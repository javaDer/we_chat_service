# coding:utf-8
# user
from flask import Blueprint, request
import shortuuid
import time
from model.model import mysql
from flaskext.mysql import MySQL
# from model.model import Online_Service

api = Blueprint('api', __name__)

su = shortuuid.ShortUUID()


@api.route('/save')
def save():
    online_username = request.args.get("username")
    online_online_type = request.args.get("type")
    online_phone = request.args.get("phone")
    online_address = request.args.get("address")
    online_time = request.args.get("online_time")
    online_Order_time = time.asctime(time.localtime(time.time()))
    cursor = mysql.get_db().cursor()
    cursor.execute('select * from users limit 5')
    data = cursor.fetchall()
    # online_repait = Online_Service(id=su.get_alphabet(), online_username=online_username,
    #                                online_online_type=online_online_type, online_phone=online_phone,
    #                                online_address=online_address, online_time=online_time, online_status=1,
    #                                online_Order_time=online_Order_time)
    # online_repait = Online_Service(su.get_alphabet(),online_username,
    #                                online_online_type, online_phone,
    #                                online_address, online_time, 1,
    #                                online_Order_time)
    # print(online_repait)
    # Online_Service.save(online_repait)
    return "save"
