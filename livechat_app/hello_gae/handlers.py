# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template
from flask import redirect, request
import pdb

hello_gae = Blueprint('hello_gae', __name__)
livechat = Blueprint('livechat', __name__)

@hello_gae.route('/')
def login():
    return render_template("login.html")

@livechat.route('/')
def chat():
    name = request.args['id']
    return render_template("liveChat.html",name=str(name))

