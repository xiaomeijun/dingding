# coding=utf-8
import requests
import time
import sys
import os

# sys.path.append(os.getcwd())
print(sys.argv)
# os.chdir(sys.argv[0])
os.chdir(sys.path[0])

time_start = time.time()
if __name__ == '__main__':
    testData = {"business": "vedio", "msg_body": "测试."}
    response = requests.post('http://10.1.254.132:5000/api/v1/sendmsg', json=testData)

print(response.text)

time_end = time.time()
print('totally cost', time_end - time_start)