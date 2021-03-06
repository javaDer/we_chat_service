from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@127.0.0.1:3306/online_jswl'
# 设置这一项是每次请求结束后都会自动提交数据库中的变动
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    user = db.relationship('User', backref='role')

    # repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    def __repr__(self):
        return '<Role {}> '.format(self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Online_Service(db.Model):
    __tablename__ = 'online_service'
    id = db.Column(db.Integer, primary_key=True)
    online_username = db.Column(db.String(12), unique=True)
    online_online_type = db.Column(db.String(16), unique=True)
    online_phone = db.Column(db.String(11), unique=True)
    online_address = db.Column(db.String(16), unique=True)
    online_time = db.Column(db.String(6), unique=True)
    online_status = db.Column(db.Integer, unique=True)
    online_Order_time = db.Column(db.String(32), unique=True)

    def __repr__(self):
        return '<Online_Service %r>' % self.online_username

    def __init__(self, id, online_username, online_online_type, online_phone, online_address, online_time,
                 online_status, online_Order_time):
        self.id = id
        self.online_username = online_username
        self.online_online_type = online_online_type
        self.online_phone = online_phone
        self.online_address = online_address
        self.online_time = online_time
        self.online_status = online_status
        self.online_Order_time = online_Order_time

    def save(self):
        db.session.add(self)
        db.session.commit()


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
