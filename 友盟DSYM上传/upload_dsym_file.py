# -*- coding: utf-8 -*-
#!/usr/bin/env python

import aop
import aop.api.biz
import json

#上传dsym文件

aop.set_default_server('getway.open.umeng.com')

#设置appKey和security
# 61727fd1e0f9bb492b3a3591
aop.set_default_appinfo(123,"234243")

req = aop.api.UmengQuickbirdSymUploadRequest()

try:
    resp = req.get_response(None, dataSourceId="5fb6001a73749c24fd9cb356", appVersion="1.0.3", fileType=1, fileName="symbol.zip")
    print(resp)
except aop.ApiError as e:
    # Api网关返回的异常
    print(e)
except aop.AopError as e:
    # 客户端Api网关请求前的异常
    print(e)
except Exception as e:
    # 其它未知异常
    print(e)