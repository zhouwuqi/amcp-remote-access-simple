from flask import Blueprint, request, jsonify
import os
import requests  
import time
import random
import string
import json
import threading
from commands import *

blueprint = Blueprint('tools', __name__)

#######################################
PASSWORD = "hD1mk90997907"
#######################################




# 向特定服务器发送json
def post_json(url, info, headers=None, timeout=30):
    try:
        default_headers = {"Content-Type": "application/json"}
        if headers:
            default_headers.update(headers)
        response = requests.post(url, json=info, headers=default_headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"POST请求失败: {str(e)}")




# ----------------------------------------------------------------
# 接受来自agentplus的普通调用
@blueprint.route('/amcp/mini-machine', methods=['POST'])
def sample_sync():

    data = request.get_json()
    params = data["params"] # 在agentplus中设置的固定输入值
    args = data["args"] # 来自agentplus的会话信息
    input = data["input"] # agent的输入

    password = params["password"]

    if(password == PASSWORD):
        # -------------------
        # 你的代码...
        if("instruction" in input.keys()):
            instruction = input["instruction"]
            if(instruction == "tell-folder"):
                if("path" in input.keys()):
                    path = input["path"]
                    returnData = command_tell_folder(path)
                else:
                    returnData = "invaild path."

            elif(instruction == "tell-process"):
                returnData = command_tell_process()

            elif(instruction == "tell-nvidia"):
                returnData = command_tell_nvidia()

            elif(instruction == "tell-memory"):
                returnData = command_tell_memory()

            elif(instruction == "tell-disk"):
                returnData = command_tell_disk()

            elif(instruction == "read-file"):
                if("path" in input.keys()):
                    path = input["path"]
                    if("row" in input.keys()):
                        row = int(input["row"])
                    else:
                        row = None
                    returnData = command_read_file(path, row)
                else:
                    returnData = "invaild path or row."
                

            elif(instruction == "search-in-file"):
                if("path" in input.keys() and "value" in input.keys()):
                    path = input["path"]
                    value = input["value"]
                    returnData = find_keyword_in_file(path, value)
                else:
                    returnData = "invaild path or value"
 
        else:
            returnData = "invaild instruction"     
        # -------------------
    else:
        returnData = "ERROR,Access Denied. please contact the amcp's provider"

    try:
        # 返回成功响应和文件名
        return jsonify({
            "statusCode": 1, 
            "returnData":returnData
        })
    except Exception as e:
        return jsonify({"statusCode": 0, "message": f"Error: {str(e)}"}), 500










