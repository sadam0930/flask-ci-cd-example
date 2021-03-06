import os
from flask import Flask, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# Create Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

debug = (os.getenv('DEBUG', 'False') == 'True')
port = os.getenv('PORT', '5000')

######################################################################
# GET INDEX
######################################################################
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Upload succesful')
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    # GET request routes here
    return app.send_static_file('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

######################################################################
# UTILITY FUNCTIONS
######################################################################
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

######################################################################
#   M A I N
######################################################################

if __name__ == "__main__":
    print "Service Starting..."
    app.run(host='0.0.0.0', port=int(port), debug=debug)
