#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/3/26 17:30 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: test.py
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
config.load_kube_config(config_file="./resource/config.yaml")
V1 = client.CoreV1Api()


def list_namespaces():
    list_namespaces = []
    for ns in V1.list_namespace().items:
        print(ns.metadata.name)


if __name__ == '__main__':
    list_namespaces()