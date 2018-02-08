from we_chat_service import db


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
    online_username = db.Column(db.String(12), index=True)
    online_online_type = db.Column(db.String(16))
    online_phone = db.Column(db.String(11))
    online_address = db.Column(db.String(16))
    online_time = db.Column(db.String(6))
    online_status = db.Column(db.Integer)
    online_Order_time = db.Column(db.String(32))

    def __repr__(self):
        return '<Online_Service {}>'.format(self.id, self.online_username, self.online_online_type, self.online_phone,
                                            self.online_address, self.online_time, self.online_status,
                                            self.online_Order_time)


if __name__ == '__main__':
    db.create_all()
