#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/3/27 12:03 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: create_deployment_from_yaml.py
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
from os import path
from app.Config import V1, V2, V3
from kubernetes import client, config, utils
config.load_kube_config(config_file='C:/PycharmProjects/Flask_kubernetes/resource/config.yaml')


def create_deployment_from_yaml():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()
    k8s_client = client.ApiClient()
    utils.create_from_yaml(k8s_client, "nginx-deployment.yaml")
    k8s_api = client.ExtensionsV1beta1Api(k8s_client)
    deps = k8s_api.read_namespaced_deployment("nginx-deployment", "default")
    print("Deployment {0} created".format(deps.metadata.name))


if __name__ == '__main__':
    create_deployment_from_yaml()