#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS

from router.api import api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/online_jswl'
# 设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
cors = CORS(app, resource={r"/api/*": {"origins": "*"}})
app.config.from_object('config')
db = SQLAlchemy(app)
app.register_blueprint(api, url_prefix='/api')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
