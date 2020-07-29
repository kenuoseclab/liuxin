from functools import wraps
from flask import redirect, url_for, session


def loginCheck(f):
    @wraps(f)
    def function(*args, **kwargs):
        try:
            if 'login' in session:
                if session['login'] == 'success':
                    return f(*args, **kwargs)
                else:
                    return redirect(url_for('login'))
            else:
                return redirect(url_for('login'))
        except Exception as e:
            print(e)
            return redirect(url_for('Error'))

    return function
