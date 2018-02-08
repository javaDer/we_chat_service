#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS
from router.Api import api
from flaskext.mysql import MySQL
app = Flask(__name__)
cors = CORS(app, resource={r"/api/*": {"origins": "*"}})
app.register_blueprint(api, url_prefix='/api')
db = SQLAlchemy(app)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
