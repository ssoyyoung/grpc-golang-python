from flask import Flask

import grpc
from gen.python.GRPCServer import GRPCServer_pb2
from gen.python.GRPCServer import GRPCServer_pb2_grpc


from concurrent import futures

app = Flask(__name__)

class Service(GRPCServer_pb2_grpc.GPRCServerServicer):
    def connectGRPC(self, request, context):
        return GRPCServer_pb2.firstResponse(msg=f'Hello, {request.name}!')
    def disconnectGRPC(self, request, context):
        return GRPCServer_pb2.lastResponse(msg=f'GoodBye, {request.name}!')
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    GRPCServer_pb2_grpc.add_GPRCServerServicer_to_server(Service(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Starting GRPC Server~~~~")
    server.wait_for_termination()



if __name__ == "__main__":
    serve()