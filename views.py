from flask import Blueprint, request, jsonify
import os
import requests  
import time
import random
import string
import json
import threading
from commands import *
from dotenv import load_dotenv

blueprint = Blueprint('tools', __name__)
load_dotenv()
#######################################
PASSWORD = os.getenv("PASSWORD")
#######################################


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

            elif(instruction == "tell-cpu"):
                returnData = command_tell_cpu()

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

            elif(instruction == "search-file"):
                if("path" in input.keys() and "value" in input.keys()):
                    path = input["path"]
                    value = input["value"]
                    returnData = command_search_file_folder(path, value)
                else:
                    returnData = "invaild path or value"


            elif(instruction == "tell-git"):
                if("path" in input.keys()):
                    path = input["path"]
                    # print("---------")
                    # print(path)
                    # print(type(path))
                    try:
                        # 两种情况都有可能
                        try:
                            owner = path["owner"]
                            repo = path["repo"]
                        except:
                            pathDict = json.loads(path)
                            owner = pathDict["owner"]
                            repo = pathDict["repo"]
                        returnData = git_read_repo(owner,repo)
                    except:
                        returnData = "invaild path,please input a json"
                    # value = input["value"]
                    
                else:
                    returnData = "invaild path or value"

            elif(instruction == "read-git-file"):
                if("path" in input.keys()):
                    path = input["path"]
                    if("row" in input.keys()):
                        row = int(input["row"])
                    else:
                        row = None
                    try:
                        # 两种情况都有可能
                        try:
                            owner = path["owner"]
                            repo = path["repo"]
                            filename =  path["filename"]
                        except:
                            pathDict = json.loads(path)
                            owner = pathDict["owner"]
                            repo = pathDict["repo"]
                            filename =  pathDict["filename"]
                        
                        returnData = git_read_file_by_rows(filename, owner, repo,row)
                    except:
                        returnData = "invaild path,please input a json"
                    # value = input["value"]
                else:
                    returnData = "invaild path or row."


            elif(instruction == "tell-git-folder"):
                if("path" in input.keys()):
                    path = input["path"] # 这个 path 是一个包含 owner, repo, folder_path 的 JSON 字符串或字典
                    try:
                        # 两种情况都有可能
                        try:
                            owner = path["owner"]
                            repo = path["repo"]
                            folder_path = path["folder_path"]
                        except:
                            pathDict = json.loads(path)
                            owner = pathDict["owner"]
                            repo = pathDict["repo"]
                            folder_path = pathDict["folder_path"]
                        
                        returnData = git_read_folder_in_repo(owner, repo, folder_path)
                    except Exception as e:
                        returnData = f"invaild path or folder_path, please input a valid json: {str(e)}"
                else:
                    returnData = "invaild path or folder_path."
                

            else:
                returnData = "no such instruction."
 
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










