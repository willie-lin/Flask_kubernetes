#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/3/27 9:43 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: example.py
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

from app.Config import V1
from kubernetes import watch,client,config
from kubernetes.client import configuration
from pick import pick


def list_namespaces():
    print("Listing pods with their IPs:")
    ret = V1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t\t\t\t%s\t\t\t\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


def watch_namespaces():
    count = 10
    w = watch.Watch()
    for event in w.stream(V1.list_namespace, timeout_seconds=10):
        print("Event: %s %s" % (event['type'], event['object'].metadata.name))
        count -= 1
        if not count:
            w.stop()
    print("Ended.")


def list_api_version():
    print("Supported APIS (* is preferred version):")
    print("%-20s %s" %
          ("core", "s".join(client.CoreApi().get_api_versions().versions)))
    for api in client.ApisApi().get_api_versions().groups:
        versions = []
        for v in api.versions:
            print(v)
            print(api.preferred_version.version)
            name = ""
            if v.version == api.preferred_version.version and len(api.versions) > 1:
                name += ""
            name += v.version
            versions.append(name)
            print("%-40s %s" % (api.name, ",".join(versions)))


# 服务器目录下自动查找配置文件
def pick_config():
    contexts, active_context = config.list_kube_config_contexts()
    if not contexts:
        print("Cannot find any context in kube-config file.")
        return
    contexts = [context['name'] for context in contexts]
    active_index = contexts.index(active_context['name'])
    option, _ = pick(contexts, title="Pick the context to load",
                     default_index=active_index)
    # Configs can be set in Configuration class directly or using helper
    # utility
    config.load_kube_config(context=option)

    print("Active host is %s" % configuration.host)

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for item in ret.items:
        print(
            "%s\t%s\t%s" %
            (item.status.pod_ip,
             item.metadata.namespace,
             item.metadata.name))


if __name__ == '__main__':
    # watch_namespaces()
    # list_api_version()
    # pick_config()
    list_namespaces()