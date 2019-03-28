# #!/usr/bin/env python
# # -*- coding:utf-8 _*-
# """
# # @Time    : 2019/3/28 16:50
# # @Author  :  林皆醉
# # @Desc : =============================================
# # @FileName: example.py
# # @Software: PyCharm
# # @Project Flask_kubernetes
# # =====================================================
# # code is far away from bugs with the god animal protecting
#     I love animals. They taste delicious.
# -----------------------------------------------------
#               ┏┓      ┏┓
#             ┏┛┻━━━┛┻┓
#             ┃      ☃      ┃
#             ┃  ┳┛  ┗┳  ┃
#             ┃      ┻      ┃
#             ┗━┓      ┏━┛
#                 ┃      ┗━━━┓
#                 ┃  神兽保佑    ┣┓
#                 ┃　永无BUG！   ┏┛
#                 ┗┓┓┏━┳┓┏┛
#                   ┃┫┫  ┃┫┫
#                   ┗┻┛  ┗┻┛
# ------------------------------------------------------
#
# """
#
#
# @app.route('/list_all_namespaces_info')
# def list_all_namespaces_info():
#     for ns in V1.list_namespace().items:
#         print(ns.metadata.name)
#     return "List"
#
# #
# # @app.route('/list_pod_for_ip')
# # def list_pod_for_ip():
# #     list_ip = []
# #     ret = V1.list_pod_for_all_namespaces(watch=False)
# #     print(ret)
# #     for i in ret.items:
# #         # list_ip = list_ip.append(i.status.pod_ip + ':' + i.metadata.namespace + ':' + i.metadata.name)
# #         # print(list_ip)
# #         print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
# #         return 'list_pod_for_ip'
#
#
# @app.route('/list_namespaces')
# def list_namespaces():
#     print("Listing pods with their IPs:")
#     ret = V1.list_pod_for_all_namespaces(watch=False)
#     for i in ret.items:
#         print("%s\t\t\t\t%s\t\t\t\t%s" %
#               (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
#     return 'list_namespaces'
#     # return 'list_namespaces'
#
#
# @app.route('/watch_namespaces')
# def watch_namespaces():
#     count = 10
#     w = watch.Watch()
#     for event in w.stream(V1.list_namespace, timeout_seconds=10):
#         print("Event: %s %s" % (event['type'], event['object'].metadata.name))
#         count -= 1
#         if not count:
#             w.stop()
#     print("Ended.")
#
#
# @app.route('/list_api_version')
# def list_api_version():
#     print("Supported APIS (* is preferred version):")
#     print("%-20s %s" %
#           ("core", "s".join(client.CoreApi().get_api_versions().versions)))
#     for api in client.ApisApi().get_api_versions().groups:
#         versions = []
#         for v in api.versions:
#             print(v)
#             print(api.preferred_version.version)
#             name = ""
#             if v.version == api.preferred_version.version and len(api.versions) > 1:
#                 name += ""
#             name += v.version
#             versions.append(name)
#             print("%-40s %s" % (api.name, ",".join(versions)))
#
#
# @app.route('/create_namespaced_ingress')
# def create_namespaced_ingress():
#     namespace = 'nginx'
#     # body = V1beta1Ingress()
#     include_uninitialized = True
#     pretty = 'pretty_example'  # str | If 'true', then the output is pretty printed. (optional)
#     dry_run = 'dry_run_example'  # str | When present, i
#
#     try:
#         api_response = V2.create_namespaced_ingress(namespace, body, include_uninitialized=include_uninitialized, pretty=pretty, dry_run=dry_run)
#         print(api_response)
#     except ApiException as e:
#         print("Exception when calling ExtensionsV1beta1Api->create_namespaced_ingress: %s\n" % e)
