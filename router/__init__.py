# coding:utf-8
from flask import Blueprint, render_template, redirect

api = Blueprint('api', __name__,)


@api.route('/save')
def save():
    return
