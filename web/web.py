import os, sys
from datetime import timedelta
from flask import Flask, render_template
from flask_wtf import CSRFProtect

sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], os.path.pardir))

from config import Ini

app = Flask(__name__)
app.config.from_object(Ini)
app.secret_key = os.urandom(64)
app.permanent_session_lifetime = timedelta(hours=6)
CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/map')
def map():
    return render_template('./pages/maps/google.html')


if __name__ == '__main__':
    app.run(threaded=True, host='127.0.0.1', port='88', debug=True)
