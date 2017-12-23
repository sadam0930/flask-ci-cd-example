import os
from flask import Flask, Response, jsonify, request, json

# Create Flask application
app = Flask(__name__)

# Status Codes
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_204_NO_CONTENT = 204
HTTP_400_BAD_REQUEST = 400
HTTP_404_NOT_FOUND = 404
HTTP_409_CONFLICT = 409

debug = (os.getenv('DEBUG', 'False') == 'True')
port = os.getenv('PORT', '5000')

######################################################################
# GET INDEX
######################################################################
@app.route('/')
def index():
    return jsonify(name='REST API Service',
                   version='0.1'
                   ), HTTP_200_OK


######################################################################
#   M A I N
######################################################################

if __name__ == "__main__":
    print "Service Starting..."
    app.run(host='0.0.0.0', port=int(port), debug=debug)
