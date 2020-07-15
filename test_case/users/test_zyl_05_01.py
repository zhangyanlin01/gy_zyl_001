import random

import requests

from config.conf import API_URL


def test_zyl_sql(db):
    # 执行查询sql语句
    res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS=0 AND account_name IS NOT NULL;")
    # 从查询结果中随机获取一条，取第一个数据
    account_name = random.choice(res)[0]
    data = {
    "accountName":account_name,
    "changeMoney":1000
     }
    # 使用requests框架发送http请求
    r = requests.post(API_URL + "/acc/charge",json=data)
    print(r.text)

