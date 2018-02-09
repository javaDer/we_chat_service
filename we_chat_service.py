#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS

from router.Api import api

app = Flask(__name__)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
cors = CORS(app, resource={r"/api/*": {"origins": "*"}})
app.register_blueprint(api, url_prefix='/api')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
