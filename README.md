[![Build Status](https://travis-ci.org/sadam0930/flask-ci-cd-example.svg?branch=master)](https://travis-ci.org/sadam0930/flask-ci-cd-example)
[![codecov](https://codecov.io/gh/sadam0930/flask-ci-cd-example/branch/master/graph/badge.svg)](https://codecov.io/gh/sadam0930/flask-ci-cd-example)

# Flask App for Image Upload

This is a demo application that creates a simple flask webserver with an API endpoint for uploading image files. Once uploaded, the image is displayed back to the user.

---
## Features
* HTML form for image upload
* RESTful API for handling image upload
* Unit test for API
* CI integration with travis-ci
* Docker container for easy deployment
```
docker build -t image upload .
docker run -d --name imageupload -p 5000:5000 --rm
```
* Procfile for deploying to heroku (non-docker)