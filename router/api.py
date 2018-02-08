# coding:utf-8
# user
from flask import Blueprint, request
import shortuuid

from model.model import Online_Service

api = Blueprint('api', __name__)

su = shortuuid.ShortUUID(alphabet="01345678")


@api.route('/save')
def save():
    user = request.args.get("username")
    service_type = request.args.get("type")
    tel = request.args.get("phone")
    address = request.args.get("address")
    online_time = request.args.get("online_time")

    online_repait = Online_Service(su.get_alphabet())
    return "save"
