# -*- coding: utf-8 -*-
"""
Module for launching main WSGI app instance.
"""

from livechat_app.app import create_app
from livechat_app import settings
from werkzeug import DebuggedApplication

flask_app = create_app(settings)

if flask_app.config['DEBUG']:
    flask_app.debug = True
    flask_app =  DebuggedApplication(flask_app, evalex=True)

app = flask_app

