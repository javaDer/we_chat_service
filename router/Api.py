# coding:utf-8
# user
import time
from flask import Blueprint, request
import shortuuid

from model.model import Online_Service

api = Blueprint('api', __name__)

su = shortuuid.ShortUUID(alphabet="01345678")


@api.route('/save')
def save():
    online_username = request.args.get("username")
    online_type = request.args.get("type")
    online_phone = request.args.get("phone")
    online_address = request.args.get("address")
    online_time = request.args.get("online_time")
    online_Order_time = time.asctime(time.localtime(time.time()))
    online_status = 1
    online_repait = Online_Service(su.get_alphabet(), online_username, online_type, online_phone, online_address,
                                   online_time, online_status, online_Order_time)
    online_repait.save()
    return "save"
