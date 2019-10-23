# -*- coding: utf-8 -*-
from functools import wraps
import hashlib
from flask import session, redirect
def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        uid = session.get('uid')
        if session.get('uid'):
            return func(*args, **kwargs)
        else:
            return redirect('/')
    return decorated_function

def generate_password_hash(s):
    m = hashlib.md5()
    b = s.encode(encoding='utf-8')
    m.update(b)
    return  m.hexdigest()