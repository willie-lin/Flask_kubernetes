#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/3/26 17:55 
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
from app.Config import V1, V2, V3, body
import kubernetes.client
from kubernetes.client.rest import ApiException
# from kubernetes import client, config
# config.load_kube_config(config_file='config.yaml')
# V1 = client.CoreV1Api()


def list_namespaces():
    for ns in V1.list_namespace().items:
        print(ns.metadata.name)


def list_pod_for_ip():
    list_ip = []
    ret = V1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        # list_ip = list_ip.append(i.status.pod_ip + ':' + i.metadata.namespace + ':' + i.metadata.name)
        # print(list_ip)
        print("%s\t%s\t%s" % (i.status.pod_ip,  i.metadata.namespace, i.metadata.name))


def create_namespaced_ingress():
    configuration = kubernetes.client.Configuration()

    api_instance = kubernetes.client.ExtensionsV1beta1Api(kubernetes.client.ApiClient(configuration))
    namespace = 'nginx'
    body = kubernetes.client.V1beta1Ingress()
    include_uninitialized = True
    pretty = 'pretty_example'  # str | If 'true', then the output is pretty printed. (optional)
    # dry_run = 'dry_run_example'  # str | When present, i
    # exact = True
    # export = 80
    print(body)

    try:
        # api_response = api_instance.create_namespaced_ingress(namespace, body, include_uninitialized=include_uninitialized, pretty=pretty, dry_run=dry_run)
        api_response = api_instance.create_namespaced_ingress(namespace, body, include_uninitialized=include_uninitialized, pretty=pretty)
        print(api_response)
    except ApiException as e:
        print("Exception when calling ExtensionsV1beta1Api->create_namespaced_ingress: %s\n" % e)


def read_namespaced_ingress():
    # Configure API key authorization: BearerToken
    configuration = kubernetes.client.Configuration()
    # configuration.api_key['authorization'] = 'YOUR_API_KEY'
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['authorization'] = 'Bearer'

    # create an instance of the API class
    api_instance = kubernetes.client.ExtensionsV1beta1Api(kubernetes.client.ApiClient(configuration))
    name = '80'  # str | name of the Ingress
    namespace = 'nginx'  # str | object name and auth scope, such as for teams and projects
    pretty = 'pretty_example'  # str | If 'true', then the output is pretty printed. (optional)
    exact = True  # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. (optional)
    export = True  # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

    try:
        api_response = api_instance.read_namespaced_ingress(name, namespace, pretty=pretty, exact=exact, export=export)
        print(api_response)
    except ApiException as e:
        print("Exception when calling ExtensionsV1beta1Api->read_namespaced_ingress: %s\n" % e)


if __name__ == '__main__':
    # list_pod_for_ip()
    # list_namespaces()
    create_namespaced_ingress()
    # read_namespaced_ingress()