# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from functools import wraps
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,ValidationError


class LoginForm(FlaskForm):
    username = StringField(
        # 标签
        label="账号",
        # 验证器
        validators=[
            DataRequired('请输入用户名')
        ],
        description="账号",
        # 附加选项,会自动在前端判别
        render_kw={
            "class":"form-control",
            "placeholder":"请输入账号!",
            "required":'required'
        }
    )

    password = PasswordField(
        # 标签
        label="密码",
        # 验证器
        validators=[
            DataRequired('请输入密码')
        ],
        description="密码",

        # 附加选项(主要是前端样式),会自动在前端判别
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
        # 标签
        label="账号",
        # 验证器
        validators=[
            DataRequired('请输入用户名')
        ],
        description="账号",
        # 附加选项,会自动在前端判别
        render_kw={
            "class":"form-control",
            "placeholder":"请输入账号!",
            "required":'required'
        }
    )

    password = PasswordField(
        # 标签
        label="密码",
        # 验证器
        validators=[
            DataRequired('请输入密码')
        ],
        description="密码",

        # 附加选项(主要是前端样式),会自动在前端判别
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
        # 标签
        label="任务标题",
        # 验证器
        validators=[
            DataRequired('请输入任务标题')
        ],
        description="任务标题",
        # 附加选项,会自动在前端判别
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

