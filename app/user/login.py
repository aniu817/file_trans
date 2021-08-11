#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/11 11:59
# @Author : liu yang
# @Desc: 登录
import json

from flask import Flask, request
from flask import Blueprint
from settings import Conf

from tools.token_tool import TokenTool
from tools.orm_tool import OrmTool
from models.user import User


login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        token = request.headers.get('token')
        account = request.json.get('account')
        password = request.json.get('password')
        db_password = OrmTool.query_by_account(User, account)

        if len(token) == 0:
            if password == db_password:
                dic = {'account': account, 'password': password}
                token = TokenTool.encrypt(dic)
                dic = {'state': 'success', 'token': token}
                return json.dumps(dic)
            else:
                return '账号密码错误，请重新输入'
        else:
            token_account = TokenTool.decrypt(token)['account']
            token_password = TokenTool.decrypt(token)['password']
            if token_account == account and token_password == password:
                dic = {'state': 'success', 'token': token}
                return json.dumps(dic)
            else:
                return '用户信息过期，请重新登录'

