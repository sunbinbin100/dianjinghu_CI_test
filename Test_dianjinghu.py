# encoding: utf-8
# @Author  : sun

import requests
# import datetime, random
# import json, logging
# import re, sys, copy, ast, time
# from prettyprinter import cpprint
# from functools import reduce
# from collections import defaultdict, OrderedDict, namedtuple, deque, Counter
# from collections.abc import Iterable, Iterator


# def get_djh_user_info(phone, r_l, typ):
#     """查看用户信息"""
#     payload = {"mobile": phone, "password": 'e10adc3949ba59abbe56e057f20f883e', 'remember_login': r_l, 'type': typ}
#     respo1 = requests.post(url='https://www.dianjinghu.com/web.php?m=home&c=login&a=log', data=payload)
#     # print(respo1.json())
#     params = {'m': 'home', 'c': 'memberNew', 'a': 'center'}
#     respo3 = requests.get(url='https://www.dianjinghu.com/web.php?m=home&c=memberNew&a=center', cookies=respo1.cookies, params=params)
#     return respo3.json()

def change_djh_nickname(nickname):
    """更改昵称"""
    payload0 = {"mobile": 15221466224, "password": 'e10adc3949ba59abbe56e057f20f883e', 'remember_login': 1, 'type': 1}
    resp1 = requests.post(url='https://www.dianjinghu.com/web.php?m=home&c=login&a=log', data=payload0)
    # print(resp1.json())
    payload1 = {"nickname": str(nickname)}
    resp2 = requests.post(url='https://www.dianjinghu.com/web.php/home/member/chNickname/', cookies=resp1.cookies, data=payload1)
    return resp2.json()


print(change_djh_nickname('陈冬123123'))


# payload0 = {"mobile": 15221466224, "password": 'e10adc3949ba59abbe56e057f20f883e', 'remember_login': 1, 'type': 1}
# resp1 = requests.post(url='https://www.dianjinghu.com/web.php?m=home&c=login&a=log', data=payload0)
# # print(resp1.json())
# payload1 = {"nickname": '帆布鞋1'}
# resp2 = requests.post(url='https://www.dianjinghu.com/web.php/home/member/chNickname/', cookies=resp1.cookies, data=payload1)
# print(resp2.json())








