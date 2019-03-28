#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/3/26 16:51 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: Config.py
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
from kubernetes import client, config
config.load_kube_config(config_file='C:/PycharmProjects/Flask_kubernetes/resource/config.yaml')
V1 = client.CoreV1Api()
V2 = client.ExtensionsV1beta1Api()
V3 = client.ApiClient()
body = client.V1beta1Ingress()