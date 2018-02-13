#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/11 21:07
# @Author  : Wendyltanpcy
# @File    : forms.py
# @Software: PyCharm


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')