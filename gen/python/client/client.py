from gen.python.GRPCServer import GRPCServer_pb2
from gen.python.GRPCServer import GRPCServer_pb2_grpc

import grpc

def client():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = GRPCServer_pb2_grpc.GPRCServerStub(channel)

        res = stub.connectGRPC(GRPCServer_pb2.firstRequest(name='so young'),timeout=2)
        res2 = stub.disconnectGRPC(GRPCServer_pb2.lastRequest(name='so young'), timeout=2)

    print(res.msg)
    print(res2.msg)

client()
