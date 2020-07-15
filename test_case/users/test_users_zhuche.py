from tools.api import request_tool


def test_qqq(pub_data):

    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    pub_data["pwd"] = "自动生成 字符串 6 数字字母"
    pub_data["userName"] = "自动生成 字符串 5 数字 zyl"
    pub_data["phone"] = "自动生成 手机号"
    json_data = '''
{
  "phone": "${phone}",
  "pwd": "${pwd}",
  "rePwd": "${pwd}",
  "userName": "${userName}"
}
'''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    json_path = [{"cstId":'$.data.cstId'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(json_path=json_path, method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)
def test_smrz(pub_data):
    pub_data["certno"] = "自动生成 身份证号"
    pub_data["cstName"] = "自动生成 姓名"
    pub_data["email"] = "自动生成 邮箱"
    header = {
        "token":pub_data["token"]
    }
    json_data = {
    "cstId": "${cstId}",
    "customerInfo": {
    "birthday": "2001-08-25",
    "certno": "${certno}",
    "city": "上海",
    "cstName": "${cstName}",
    "email": "${email}",
    "province": "上海市",
    "sex": 2
    }
    }
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = 'smrz'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/realname2"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data,
                         status_code=status_code,expect=expect, feature=feature, story=story, title=title, headers=header)