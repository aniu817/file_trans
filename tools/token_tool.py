#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/11 16:53
# @Author : liu yang
# @Desc:  token 工具


from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from settings import Conf


class TokenTool:
    _serializer = Serializer(Conf.SECRET_KEY.value, 3600)

    @staticmethod
    def encrypt(content):
        """

        :param content: dic 类型
        :return:
        """
        token = TokenTool._serializer.dumps(content).decode('utf-8')
        return token

    @staticmethod
    def decrypt(token):
        return TokenTool._serializer.loads(token)


if __name__ == "__main__":
    token = TokenTool.encrypt({'name': 'liuyang'})
    TokenTool.decrypt(token)

