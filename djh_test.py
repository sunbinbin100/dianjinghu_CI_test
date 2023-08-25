# encoding: utf-8

import requests
import argparse, os, sys
# import datetime, random
import json, logging
# import re, sys, copy, ast, time
from prettyprinter import cpprint
# from functools import reduce
# from collections import defaultdict, OrderedDict, namedtuple, deque, Counter
# from collections.abc import Iterable, Iterator

# def get_djh_user_info(phone, r_l, typ):


def change_djh_nickname(mobile, nickname):
    """更改昵称接口"""
    # 先登录，提供cookie
    payload0 = {"mobile": mobile, "password": 'e10adc3949ba59abbe56e057f20f883e', 'remember_login': 1, 'type': 1}
    resp1 = requests.post(url='https://www.dianjinghu.com/web.php?m=home&c=login&a=log', data=payload0)
    # print(resp1.json())
    payload1 = {"nickname": str(nickname)}
    resp2 = requests.post(url='https://www.dianjinghu.com/web.php/home/member/chNickname/', cookies=resp1.cookies, data=payload1)
    # 输出用户信息，查看更改昵称是否成功
    params1 = {'m': 'home', 'c': 'memberNew', 'a': 'center'}
    resp3 = requests.get(url='https://www.dianjinghu.com/web.php?m=home&c=memberNew&a=center', cookies=resp1.cookies, params=params1)
    cpprint(resp3.json())
    return resp2.json()

# 获取命令行输入的参数（3种方法：https://zhuanlan.zhihu.com/p/508646581、https://blog.csdn.net/shawnchang777/article/details/112471573）
# print('sys.argv方法 获取到的参数列表为:', sys.argv)  # 列表。参数个数 应对应 jenkins里的Windows batch command中的参数个数
# phone_number, nick_name = sys.argv[1], sys.argv[2]
# print(change_djh_nickname(phone_number, nick_name))


# 创建解析器：parser
parser = argparse.ArgumentParser(description="用法：python djh_test.py --mobile xxx --nickname xxx。用-还是--具体看代码中的写法")
parser.add_argument('--mobile', default=15221466224, action='store', required=False, help='用户手机号')  # 添加参数
parser.add_argument('--nickname', default='帆布鞋丶丶丶', required=False, help='要改的昵称')
# 参数前的--也可以用-，调用时与代码里写的一致即可
# action：指定参数时可以触发六种操作。可不填，不填时，效果同action='store'
# 调用参数时，参数名可不写全，会自动识别（所以，有参数都是m开头的单词时，就不能用--m了）
# default不写时，默认值为None。help：添加参数说明
# required：为True时，调用时，参数必填；为False时，调用时，可填可不填。   required=xxx可不写，不写时，效果同False
# 调用命令(执行路径须为文件所在目录，否则须切换路径)：1、python djh_test.py 2、python djh_test.py --mobile xxx --nickname xxx

# 输入的参数默认为字符串。要改为其他类型，可用选项“type”
# parser.add_argument('--a', default=5, type=int)
# choices提供可选参数值。   注意：choices=range(2,11)意思是可选值为[2, 3, 4, 5, 6, 7, 8, 9, 10]，不是限定 实参 的长度
# parser.add_argument('--mode', default='train', choices=['train', 'predict'])

args = parser.parse_args()  # 解析参数
print('argparse库 获取到的参数为:', args.mobile, args.nickname)  # 类型分别为int和str。也可以用args.__dict__.items()取值
phone_number1, nick_name1 = args.mobile, args.nickname
print(change_djh_nickname(phone_number1, nick_name1))


# PS：jenkins里用Boolean Parameter时，布尔值都是小写的：true/false。且最后都会以字符串形式存在列表中，如：['djh_test.py', '15221466224', 'true']）
# 想要变成python中的布尔值True和False，可以用语句判断一下，如：if a1 == 'true':  a1 = True


# if __name__ == "__main__":
#     list1 = list()
#     for k, v in args.__dict__.items():  # 打印参数。也可以用 for item in args.__dict__.items()，item为 包含参数和值 的元组
#         list1.append(v)
#     print(list1)








