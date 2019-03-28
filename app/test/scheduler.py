#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/3/27 14:26 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: scheduler.py
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
import random

from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException
config.load_kube_config(config_file='C:/PycharmProjects/Flask_kubernetes/resource/config.yaml')

v1 = client.CoreV1Api()

scheduler_name = 'my-custom-scheduler-v1'

def nodes_available():
    ready_nodes = []
    for n in v1.list_node().items:
        for status in n.status.conditions:
            if status.status == 'True' and status.type == 'Ready':
                ready_nodes.append(n.metadata.name)
    return ready_nodes

def scheduler(name, node, namespace='default'):
    body = client.V1Binding()
    target = client.V1ObjectReference()
    target.kind = 'Node'
    target.apiVersion = 'v1'
    target.name = node
    meta = client.V1ObjectMeta()
    meta.name = name
    body.target = target
    body.metadata = meta
    return v1.create_namespaced_binding(name, namespace, body)

def main():
    w = watch.Watch()
    for event in w.stream(v1.list_namespaced_pod, 'default'):
        if event['object'].status.phase == 'Pending' and event['object'].spec.scheduler_name == scheduler_name:
            print("Pending Found")
            try:
                res = scheduler(event['object'].metadata.name,random.choice(nodes_available()))
                print("success")
            except Exception as a:
                print(111)
                # print (Exception when calling ->create_namespaced_binding: %s\n % a)
                # print (Exception when calling ->create_namespaced_binding: %s\n % a)