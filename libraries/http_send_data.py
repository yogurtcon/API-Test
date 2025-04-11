from google.protobuf.json_format import MessageToDict
from api_tests.resources.proto.rpcMessage.ext_pb2 import RPCOutput, RPCInput
import requests

def http_send_data(pd_obj, pb, obj, func, httpUrl='https://xxx.com',
                headers='', login_key='', if_rsp=True):
    req = pb.SerializeToString()
    pb_d = RPCInput()
    pb_d.obj = obj
    pb_d.func = func
    pb_d.req = req
    pb_d.opt['xxx'] = "xxx"
    pb_d.opt['yyy'] = "yyy"
    pb_d.opt['zzz'] = "zzz"
    pb_d.opt['X-Token'] = "xxx"
    res = requests.post(httpUrl, pb_d.SerializeToString())
    message_output = RPCOutput()
    message_output.ParseFromString(res.content)
    message = pd_obj()
    message.ParseFromString(message_output.rsp)
    print(f"接口返回完整信息：{MessageToDict(message_output)}")
    return MessageToDict(message)