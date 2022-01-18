# coding=utf-8
# !flask/bin/python
from flask import Flask, request
import json
import requests

app = Flask(__name__)
# 只接受POST方法访问
@app.route("/api/v1/sendmsg", methods=["POST"])
def check():
    # 默认返回内容
    return_dict = {'statusCode': '200', 'message': 'successful!', 'result': False}
    # 判断入参是否为空
    if request.get_data() is None:
        return_dict['statusCode'] = '5004'
        return_dict['message'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)

    get_data = request.get_data()  # 获取传入的参数
    get_data = json.loads(get_data)  # 传入的参数为bytes类型，需要转化成json
    business = get_data.get('business')
    msg_body = get_data.get('msg_body')

    return_dict['result'] = tt(business, msg_body)  # 对参数进行操作
    #webhook = 'https://oapi.dingtalk.com/robot/send?access_token=efa2ec3346c28cce4559cba2dee2099effd04ac63d811f33578c614a52958a2b'
    dis = ""
    erp = ""
    bigdata = ""
    jtservers = ""

    webhook = 'https://oapi.dingtalk.com/robot/send?access_token='

    if business == "dispatch":
      dingtalk(business, webhook + dis, msg_body)
      return json.dumps(return_dict, ensure_ascii=False)
    elif business == "erp" or business == "tmp":
      dingtalk(business, webhook + erp, msg_body)
      return json.dumps(return_dict, ensure_ascii=False)
    elif business == "bigdata":
      dingtalk(business, webhook + bigdata, msg_body)
      return json.dumps(return_dict, ensure_ascii=False)
    elif business == "vedio":
      dingtalk(business, webhook + jtservers, msg_body)
      return json.dumps(return_dict, ensure_ascii=False)

    else:
      return "error name project"

# 功能函数
def tt(name, age):
    result_str = "%s服务%s警告" % (name, age)
    return result_str

def dingtalk(msg,webhook, message):
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = {'msgtype': 'text', 'text': {'title': msg,      "content": message
                ,'messageUrl':'http://请求IP+端口号'}, 'at': {'atMobiles': ['群消息@的用户1','群消息@的用户2'], 'isAtAll': False}}
        post_data = json.dumps(data)
        response = requests.post(webhook, headers=headers, data=post_data)
        return response.text

if __name__ == "__main__":
    app.run(
    debug=True,
    host ='0.0.0.0',
    port = 5000,
    )
