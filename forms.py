# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from functools import wraps
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,ValidationError


class LoginForm(FlaskForm):
    username = StringField(
        label="账号",
        validators=[
            DataRequired('请输入用户名')
        ],
        description="账号",
        render_kw={
            "class":"form-control",
            "placeholder":"请输入账号!",
            "required":'required'
        }
    )

    password = PasswordField(
        label="密码",
        validators=[
            DataRequired('请输入密码')
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码!",
            "required": 'required'
        }
    )

    submit = SubmitField(
        label="登录",
        render_kw={
            "class": "btn btn-primary btn-flat",
        }
    )


class RegisterForm(FlaskForm):
    username = StringField(
        label="账号",
        validators=[
            DataRequired('请输入用户名')
        ],
        description="账号",
        render_kw={
            "class":"form-control",
            "placeholder":"请输入账号!",
            "required":'required'
        }
    )

    password = PasswordField(
        label="密码",
        validators=[
            DataRequired('请输入密码')
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码!",
            "required": 'required'
        }
    )

    submit = SubmitField(
        label="登录",
        render_kw={
            "class": "btn btn-primary btn-flat",
        }
    )


class PostWorkForm(FlaskForm):
    title = StringField(
        label="任务标题",
        validators=[
            DataRequired('请输入任务标题')
        ],
        description="任务标题",
        render_kw={
            "class":"form-control",
            "placeholder":"请输入任务标题!",
            "required":'required'
        }
    )


    submit = SubmitField(
        label="发布",
        render_kw={
            "class": "btn btn-primary  btn-flat",
        }
    )

