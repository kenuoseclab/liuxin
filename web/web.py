import os, sys
from datetime import timedelta
from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf.csrf import CSRFProtect, CSRFError
from lib.loginCheck import loginCheck

sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], os.path.pardir))

from config import Ini

app = Flask(__name__)
app.config.from_object(Ini)
app.secret_key = os.urandom(64)
app.permanent_session_lifetime = timedelta(hours=6)
CSRFProtect(app)


@app.route('/')
@loginCheck
def index():
    return render_template('index.html')


@app.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'GET':
        return render_template('sign-in.html')
    else:
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if username == app.config.get('WEBUSERNAME') and password == app.config.get('WEBPASSWORD'):
            session['login'] = 'success'
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))


@app.route('/logout')
@loginCheck
def Logout():
    del session['login']
    return redirect(url_for('login'))


@app.route('/config', methods=['get', 'post'])
@loginCheck
def Config():
    if request.method == 'GET':
        q = request.args.get('q', '')
        if q == 'assetscan':
            return render_template('formAsset.html')
        if q == 'vulscan':
            return render_template('formVul.html')
    else:
        pass


@app.route('/test')
def test():
    return render_template('index.html')


@app.route('/error')
def Error():
    return render_template('500.html')


@app.route('/notFound')
def NotFound():
    return render_template('404.html')


@app.errorhandler(CSRFError)
def csrfError(e):
    print('csrf handle error {}.'.format(e))
    return redirect(url_for('Error'))


if __name__ == '__main__':
    app.run(threaded=True, host='127.0.0.1', port='88', debug=True)
