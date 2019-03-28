#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/3/27 11:30 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: create_deployment.py.py
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

from  os import path
from app.Config import V2
import yaml
from kubernetes import client, config


def load_xx_yaml():
    with open(path.join((path.abspath(path.dirname(path.dirname(__file__)))), "nginx-deployment.yaml")) as f:
        dep = yaml.safe_load(f)
        k8s_beta = V2
        resp = k8s_beta.create_namespaced_deployment(body = dep, namespace="default")
        print("Deployment created. status='%s'" % str(resp.status))


if __name__ == '__main__':
    load_xx_yaml()