# -*- coding: utf-8 -*-
"""
App factory module.
"""

from flask import Flask

def create_app(config):    
    app = Flask(__name__)
    app.config.from_object(config)

    # Later register blueprints here.
    # ...
    from livechat_app.hello_gae.handlers import hello_gae,livechat

    app.register_blueprint(hello_gae, url_prefix="/")
    app.register_blueprint(livechat, url_prefix="/chat")
    return app

