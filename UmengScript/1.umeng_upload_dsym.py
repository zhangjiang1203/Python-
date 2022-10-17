import aop
import aop.api
import json



#获取当前数据参数

def testUmeng():
    # 设置网关域名
    aop.set_default_server('gateway.open.umeng.com')

    # 设置apiKey和apiSecurity
    aop.set_default_appinfo(12344, "xxxxxxxxxx")

    # 构造Request和访问协议是否是https
    req = aop.api.UmengQuickbirdSymUploadRequest()
    req = aop

    # try:
        # resp = req.get_response(None,data)


def main():
    print("你好")
    # print('获取参数个数',len(sys.argv))
    # print('参数列表',str(sys.argv))
    # name = sys.argv[1]
    # print("第一个参数",name)



if __name__ == '__main__':
    main("你好")