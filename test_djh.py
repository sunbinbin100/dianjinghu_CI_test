# encoding: utf-8

import requests
# import datetime, random
# import json, logging
# import re, sys, copy, ast, time
from prettyprinter import cpprint
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

def change_djh_nickname(mobile, nickname):
    """更改昵称"""
    payload0 = {"mobile": mobile, "password": 'e10adc3949ba59abbe56e057f20f883e', 'remember_login': 1, 'type': 1}
    resp1 = requests.post(url='https://www.dianjinghu.com/web.php?m=home&c=login&a=log', data=payload0)
    # print(resp1.json())
    payload1 = {"nickname": str(nickname)}
    resp2 = requests.post(url='https://www.dianjinghu.com/web.php/home/member/chNickname/', cookies=resp1.cookies, data=payload1)
    # 输出用户信息，查看更改昵称是否成功
    params = {'m': 'home', 'c': 'memberNew', 'a': 'center'}
    resp3 = requests.get(url='https://www.dianjinghu.com/web.php?m=home&c=memberNew&a=center', cookies=resp1.cookies, params=params)
    cpprint(resp3.json())
    return resp2.json()


print(change_djh_nickname(15221466224, 'sun21'))


# if __name__ == "__main__":
#     print(change_djh_nickname(15221466224, 'sun20'))









