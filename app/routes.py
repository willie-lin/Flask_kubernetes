#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/3/26 16:03 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: routes.py
# @Software: PyCharm
# @Project Flask_kubernetes 
# =====================================================
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
-----------------------------------------------------
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
------------------------------------------------------

"""

from app import app
from flask import render_template, flash, redirect, url_for
from wtforms import ValidationError

import requests, urllib, json
from flask import Flask, render_template, request

from kubernetes.client.rest import ApiException
from app.Config import V1, V2, body
from app.Config import V1
from kubernetes import watch,client,config
from kubernetes.client import configuration
from pick import pick
# from kubernetes import client, config
# config.load_kube_config(config_file='./resource/config.yaml')
# V1 = client.CoreV1Api()


@app.route('/')
@app.route('/index')
# @app.route('/', methods=['GET', 'POST'])
def index():
    metadata_data = []
    deployments = 'http://172.19.19.18:8080/apis/extensions/v1beta1/deployments'
    deployments_rollback = 'http://172.19.19.18:8080/apis/extensions/v1beta1/deployments/rollback'
    deployments_status = 'http://172.19.19.18:8080/apis/extensions/v1beta1/deployments/status'
    ingresses = 'http://172.19.19.18:8080/apis/extensions/v1beta1/ingresses'
    ingresses_status = 'http://172.19.19.18:8080/apis/extensions/v1beta1/ingresses/status'
    networkpolicies = 'http://172.19.19.18:8080/apis/extensions/v1beta1/networkpolicies'
    podsecuritypolicies = 'http://172.19.19.18:8080/apis/extensions/v1beta1/podsecuritypolicies'
    replicasets = 'http://172.19.19.18:8080/apis/extensions/v1beta1/replicasets'
    replicasets_scale = 'http://172.19.19.18:8080/apis/extensions/v1beta1/replicasets/scale'
    replicasets_status = 'http://172.19.19.18:8080/apis/extensions/v1beta1/replicasets/status'
    replicationcontrollers = 'http://172.19.19.18:8080/apis/extensions/v1beta1/replicationcontrollers'
    replicationcontrollers_scale = 'http://172.19.19.18:8080/apis/extensions/v1beta1/replicationcontrollers/scale'

    r0 = requests.get(deployments).json()
    r1 = requests.get(deployments_rollback).json()
    r2 = requests.get(deployments_status).json()
    r3 = requests.get(ingresses).json()
    r4 = requests.get(ingresses_status).json()
    r5 = requests.get(networkpolicies).json()
    r6 = requests.get(podsecuritypolicies).json()
    r7 = requests.get(replicasets).json()
    r8 = requests.get(replicasets_scale).json()
    r9 = requests.get(replicasets_status).json()
    r10 = requests.get(replicationcontrollers).json()
    r11 = requests.get(replicationcontrollers_scale).json()

    print('-------------------------------------------------------------')

    print(r5)
    r = json.load(r5)
    print(r)

    # print(r3)
    # name = [(item.get('name', 'Na')) for item in r5['item']]
    metadata = {
        'kind': r5['kind'],
        'apiVersion': r5['apiVersion'],
        'selfLink': r5['metadata']['selfLink'],
        'resourceVersion':r5['metadata']['resourceVersion'],
        'items': [{
            'name': r5['items'][0]['metadata']['name'],
            'namespace': r5['items'][0]['metadata']['namespace'],
            'selfLink': r5['items'][0]['metadata']['selfLink'],
            'uid': r5['items'][0]['metadata']['uid'],
            'generation': r5['items'][0]['metadata']['generation'],
            'creationTimestamp': r5['items'][0]['metadata']['creationTimestamp'],
            'resourceVersion': r5['items'][0]['spec']['resourceVersion'],
            'resourceVersion': r5['items'][0]['spec']['resourceVersion'],
            'resourceVersion': r5['items'][0]['spec']['resourceVersion'],
        }],
        # item
        # 'name':[(item.get('name', 'Na')) for item in r5['item']]
        # 'items':r5['items'][0]['metadata'],
        # 'name':r5['items']['metadata'][0]['name'],
        # 'name': r5['items'][0],
        # 'names': r5['items'][1]
    }

    # items = {
    #     'item': r5['items'],
    # }

    # print(items)
    print(metadata)

    return "Hello World!!!"




