from api_tests.resources.proto.AAA_pb2 import AAAReq, AAARes
from api_tests.libraries.http_send_data import http_send_data

class AAA:
    def aaa_aaa(self, character_id):
        pb = AAAReq()
        pb.character_id = int(character_id)
        message = http_send_data(AAARes, pb, "xxx.xxx.xxx",
                                "AAA", if_rsp=True)
        return message 