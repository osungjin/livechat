# coding=utf-8
from flask import request
from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
import pusher
import urllib
import pdb

app = Flask(__name__)

p = pusher.Pusher(
    app_id='79401',
    key='b730e31b0e4649bea071',
    secret='741c4f6286d7835824a5'
)
@app.route('/push_msg/')
def push_msg():
    curr_msg = urllib.unquote(request.query_string)
    p['test_channel'].trigger('my_event', {'message': curr_msg})
    return 'ok'

if __name__ ==  '__main__':
    app.run(debug=True,host='100.79.82.16', port=5455, threaded=True)
