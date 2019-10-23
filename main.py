# -*- coding: utf-8 -*-
from flask import Flask, redirect, session
from flask import request
from flask.templating import render_template
from flask.helpers import url_for
import pymysql
import datetime
import urllib
import json
import os
from multiprocessing import Process
import time
import random
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,ValidationError
from forms import LoginForm, RegisterForm, PostWorkForm
from common import login_required, generate_password_hash
from work import add_job, init_works
import  threading
import queue
import schedule
import time


db = pymysql.connect(host="127.0.0.1", user="root", passwd='root', db='homework')
cur = db.cursor()
app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)

work_queue = queue.Queue(10)

def job():
    if not work_queue.empty():
        sql_update = """
            UPDATE works SET status = '1' WHERE status='0' && id = '%s'
        """
        w = work_queue.get(block=False)
        if w:
            cur.execute(sql_update % (w,))
            db.commit()

            time.sleep(10)
            sql_update = """
                UPDATE works SET status = '2' WHERE status = '1' && id = '%s'
            """
            cur.execute(sql_update % (w, ))
            db.commit()
            work_queue.task_done()
        # work_queue.task_done()

def add_job(work):
    print("add job")
    print(work)
    work_queue.put(str(work))
    print(work_queue.qsize())

def work_threading():
    while True:
        print("正在运行")
        schedule.run_pending()
        time.sleep(1)

def init_works():
    sql = """select id,status,title from works where status='0' or  status='1' """
    cur.execute(sql)
    results = cur.fetchall()
    for x in results:
        add_job(x[0])

    schedule.every(5).seconds.do(job)
    worker_thread = threading.Thread(target=work_threading)
    worker_thread.start()

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        data = form.data
        print("提交")
        username=data['username']
        password=data['password']
        password=generate_password_hash(password)
        sql = """select id,username,password from users where username='%s' and password='%s' """ % (username, password)
        cur.execute(sql)
        results = cur.fetchone()

        if results:
            uid, uname, _ = results
            session['username'] = uname
            session['uid'] = uid
            return redirect('/works')
            db.close()
        else:
            return redirect('/register')
            db.close()

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        username = data['username']
        password = md5(data['password'])
        rename = """
            select * from users where username='%s'
            """
        n = cur.execute(rename % username)
        db.commit()
        if n <= 0:
            sql_insert = """
                 insert into users(username, password) values('%s','%s')
                                    """
            cur.execute(sql_insert % (username, password))
            db.commit()
            return redirect('/')
        else:
            return redirect('/')
        db.close()

    return render_template('registration.html')

@login_required
@app.route('/works', methods=['GET'])
def works():

    sql = """
        select * from works where user_id='%d'
        """
    status = {
        0: '等待运行中',
        1: '正在运行',
        2: '已经完成',
    }
    n = cur.execute(sql % session.get('uid'))
    results = cur.fetchall()
    return render_template('works.html', data=results, status=status)

@login_required
@app.route('/work_create', methods=['GET', 'POST'])
def work_create():
    form = PostWorkForm()
    if form.validate_on_submit():
        data = form.data
        title = data['title']
        sql_insert = """
            insert into works(user_id, title) values('%s','%s')
        """
        cur.execute(sql_insert % (session.get('uid'), title))
        db.commit()
        add_job(cur.lastrowid)
        return redirect('/works');
    return render_template('works_create.html', form=form)





init_works()
app.run('127.0.0.1', port=6789, debug=True)

