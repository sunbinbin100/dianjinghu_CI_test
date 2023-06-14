import datetime
import json, logging
import random, requests
import re, sys, copy, ast, time
from prettyprinter import cpprint
from functools import reduce
from collections import defaultdict, OrderedDict, namedtuple, deque, Counter
from collections.abc import Iterable, Iterator


# 测试用
def get_djh_user_info(phone, r_l, typ):
    payload0 = {"mobile": phone, "password": 'e10adc3949ba59abbe56e057f20f883e', 'remember_login': r_l, 'type': typ}
    respo1 = requests.post(url='https://www.dianjinghu.com/web.php?m=home&c=login&a=log', data=payload0)
    # print(respo1.json())
    params = {'m': 'home', 'c': 'memberNew', 'a': 'center'}
    respo3 = requests.get(url='https://www.dianjinghu.com/web.php?m=home&c=memberNew&a=center', cookies=respo1.cookies, params=params)
    return respo3.json()
    # 更改昵称：{"nickname": "帆布鞋丶"}   web.php/home/member/chNickname/


cpprint(get_djh_user_info(15221466224, 1, 1))







