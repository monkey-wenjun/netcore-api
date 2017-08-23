#!/usr/bin/env python
#-*-coding:utf-8

import requests
import json


# 获取token
def returnToken(app_key,app_secret):

    api = 'https://open.c.163.com/api/v1/token'

    payload = {"app_key":app_key,"app_secret":app_secret}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", api, data=json.dumps(payload), headers=headers)
    token = response.text # 输出的是<type 'unicode'>
    tokenInfo = json.JSONDecoder().decode(token) # 转换成json格式
    return tokenInfo["token"]

#获取镜像
def getpubimages(token):

    api ='https://open.c.163.com/api/v1/vm/publicimages?pageSize=4&pageNum=1&keyword=os&Type=linux'
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'Authorization':'Token '+token
    }
    response = requests.request("GET",api,headers=headers)
    tokenInfo = json.JSONDecoder().decode(response.text)
    imagesid = tokenInfo["images"][0]['imageId']
    return imagesid


# 创建虚拟机
def createvm(tokenValue,instance_name,ssh_key_names,image_id,cpu_weight,memory_weight,ssd_weight):

    api = 'https://open.c.163.com/api/v1/vm'
    payload = {
    "bill_info":"HOUR",
    "server_info":{
        "instance_name":instance_name,
        "ssh_key_names":[ssh_key_names],
        "image_id":image_id,
        "cpu_weight":cpu_weight,
        "memory_weight":memory_weight,
        "ssd_weight":ssd_weight,
    }
    }

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'Authorization':'Token '+tokenValue
    }
    serveresponse = requests.request("POST", api, data=json.dumps(payload), headers=headers)
    serverid = json.JSONDecoder().decode(serveresponse.text)  # 转换成json格式
    print serverid

def listvm():

    api = 'https://open.c.163.com/api/v1/vm/allInstanceInfo?pageSize=4&pageNum=1'
    headers = {
        'cache-control': "no-cache",
        'Authorization': 'Token ' + tokenValue
    }
    listvm = requests.request("GET", api, headers=headers)
    return listvm.json()

def createsshkey(token,name):
    api = 'https://open.c.163.com/api/v1/secret-keys'
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'Authorization': 'Token ' + token
    }
    payload =  {"key_name": name}
    response = requests.request("POST", api, data=json.dumps(payload), headers=headers)
    sshkey = response.text  # 输出的是<type 'unicode'>
    sshKeyInfo = json.JSONDecoder().decode(sshkey)  # 转换成json格式
    return sshKeyInfo

def getsshkey(token):
    api = 'https://open.c.163.com/api/v1/secret-keys'
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'Authorization': 'Token ' + token
    }
    response = requests.request("GET", api, headers=headers)

    sshkey = response.text  # 输出的是<type 'unicode'>
    sshKeyInfo = json.JSONDecoder().decode(sshkey)  # 转换成json格式
    sshKeyInfo = str(sshKeyInfo[0]['name'])
    return sshKeyInfo





tokenValue = returnToken("  ","  ")
print tokenValue
instance_name = 'centos7'
ssh_key_names = getsshkey(tokenValue)
image_id =getpubimages(tokenValue)
cpu_weight= 1
memory_weight = 2
ssd_weight = 20

# createvm(tokenValue,instance_name,ssh_key_names,image_id,cpu_weight,memory_weight,ssd_weight)
listvm()