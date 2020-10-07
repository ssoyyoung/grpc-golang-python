# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import GRPCServer2_pb2 as protos_dot_GRPCServer2__pb2


class GPRCServerStub(object):
    """service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.connectGRPC = channel.unary_unary(
                '/GPRCServer2.GPRCServer/connectGRPC',
                request_serializer=protos_dot_GRPCServer2__pb2.firstRequest.SerializeToString,
                response_deserializer=protos_dot_GRPCServer2__pb2.firstResponse.FromString,
                )
        self.disconnectGRPC = channel.unary_unary(
                '/GPRCServer2.GPRCServer/disconnectGRPC',
                request_serializer=protos_dot_GRPCServer2__pb2.lastRequest.SerializeToString,
                response_deserializer=protos_dot_GRPCServer2__pb2.lastResponse.FromString,
                )


class GPRCServerServicer(object):
    """service definition
    """

    def connectGRPC(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def disconnectGRPC(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GPRCServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'connectGRPC': grpc.unary_unary_rpc_method_handler(
                    servicer.connectGRPC,
                    request_deserializer=protos_dot_GRPCServer2__pb2.firstRequest.FromString,
                    response_serializer=protos_dot_GRPCServer2__pb2.firstResponse.SerializeToString,
            ),
            'disconnectGRPC': grpc.unary_unary_rpc_method_handler(
                    servicer.disconnectGRPC,
                    request_deserializer=protos_dot_GRPCServer2__pb2.lastRequest.FromString,
                    response_serializer=protos_dot_GRPCServer2__pb2.lastResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GPRCServer2.GPRCServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GPRCServer(object):
    """service definition
    """

    @staticmethod
    def connectGRPC(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GPRCServer2.GPRCServer/connectGRPC',
            protos_dot_GRPCServer2__pb2.firstRequest.SerializeToString,
            protos_dot_GRPCServer2__pb2.firstResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def disconnectGRPC(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GPRCServer2.GPRCServer/disconnectGRPC',
            protos_dot_GRPCServer2__pb2.lastRequest.SerializeToString,
            protos_dot_GRPCServer2__pb2.lastResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
