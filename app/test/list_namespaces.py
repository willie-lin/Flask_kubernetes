#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/3/27 20:57 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: list_namespaces.py
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


def list_namespaced_deployment_with_http_info(self, namespace, **kwargs):
    """
           list or watch objects of kind Deployment
           This method makes a synchronous HTTP request by default. To make an
           asynchronous HTTP request, please pass async_req=True
           >>> thread = api.list_namespaced_deployment_with_http_info(namespace, async_req=True)
           >>> result = thread.get()

           :param async_req bool
           :param str namespace: object name and auth scope, such as for teams and projects (required)
           :param bool include_uninitialized: If true, partially initialized resources are included in the response.
           :param str pretty: If 'true', then the output is pretty printed.
           :param str _continue: The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
           :param str field_selector: A selector to restrict the list of returned objects by their fields. Defaults to everything.
           :param str label_selector: A selector to restrict the list of returned objects by their labels. Defaults to everything.
           :param int limit: limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
           :param str resource_version: When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.
           :param int timeout_seconds: Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
           :param bool watch: Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
           :return: ExtensionsV1beta1DeploymentList
                    If the method is called asynchronously,
                    returns the request thread.
           """

    all_params = ['namespace', 'include_uninitialized', 'pretty', '_continue', 'field_selector', 'label_selector',
                  'limit', 'resource_version', 'timeout_seconds', 'watch']
    all_params.append('async_req')
    all_params.append('_return_http_data_only')
    all_params.append('_preload_content')
    all_params.append('_request_timeout')

    params = locals()
    for key, val in iteritems(params['kwargs']):
        if key not in all_params:
            raise TypeError(
                "Got an unexpected keyword argument '%s'"
                " to method list_namespaced_deployment" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'namespace' is set
    if ('namespace' not in params) or (params['namespace'] is None):
        raise ValueError("Missing the required parameter `namespace` when calling `list_namespaced_deployment`")

    collection_formats = {}

    path_params = {}
    if 'namespace' in params:
        path_params['namespace'] = params['namespace']

    query_params = []
    if 'include_uninitialized' in params:
        query_params.append(('includeUninitialized', params['include_uninitialized']))
    if 'pretty' in params:
        query_params.append(('pretty', params['pretty']))
    if '_continue' in params:
        query_params.append(('continue', params['_continue']))
    if 'field_selector' in params:
        query_params.append(('fieldSelector', params['field_selector']))
    if 'label_selector' in params:
        query_params.append(('labelSelector', params['label_selector']))
    if 'limit' in params:
        query_params.append(('limit', params['limit']))
    if 'resource_version' in params:
        query_params.append(('resourceVersion', params['resource_version']))
    if 'timeout_seconds' in params:
        query_params.append(('timeoutSeconds', params['timeout_seconds']))
    if 'watch' in params:
        query_params.append(('watch', params['watch']))

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params['Accept'] = self.api_client. \
        select_header_accept(
        ['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', 'application/json;stream=watch',
         'application/vnd.kubernetes.protobuf;stream=watch'])

    # HTTP header `Content-Type`
    header_params['Content-Type'] = self.api_client. \
        select_header_content_type(['*/*'])

    # Authentication setting
    auth_settings = ['BearerToken']

    return self.api_client.call_api('/apis/extensions/v1beta1/namespaces/{namespace}/deployments', 'GET',
                                    path_params,
                                    query_params,
                                    header_params,
                                    body=body_params,
                                    post_params=form_params,
                                    files=local_var_files,
                                    response_type='ExtensionsV1beta1DeploymentList',
                                    auth_settings=auth_settings,
                                    async_req=params.get('async_req'),
                                    _return_http_data_only=params.get('_return_http_data_only'),
                                    _preload_content=params.get('_preload_content', True),
                                    _request_timeout=params.get('_request_timeout'),
                                    collection_formats=collection_formats)