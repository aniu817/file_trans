#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/11 11:59
# @Author : liu yang
# @Desc: 登录
import json

from flask_restful import Resource, reqparse
from flask import jsonify

from tools.token_tool import TokenTool
from tools.orm_tool import OrmTool
from models.user import User


class Login(Resource):

    @staticmethod
    def post():
        parse = reqparse.RequestParser()
        parse.add_argument('account', type=str, help='用户名不正确', trim=True)
        parse.add_argument('password', type=str, help='密码不正确', trim=True)
        parse.add_argument('token', type=str, help='密码不正确', trim=True)
        args = parse.parse_args()
        token = args.get('token')
        account = args.get('account')
        password = args.get('password')
        db_password = OrmTool.query_by_account(User, account)

        if len(token) == 0:
            if password == db_password:
                dic = {'account': account, 'password': password}
                token = TokenTool.encrypt(dic)
                dic = {'state': 'success', 'token': token}
                return json.dumps(dic)
            else:
                return jsonify({'state': 'false', 'info': '账号密码错误，请重新输入'})
        else:
            token_account = TokenTool.decrypt(token)['account']
            token_password = TokenTool.decrypt(token)['password']
            if token_account == account and token_password == password:
                dic = {'state': 'success', 'token': token}
                return json.dumps(dic)
            else:
                return jsonify({'state': 'false', 'info': '用户信息过期，请重新登录'})

