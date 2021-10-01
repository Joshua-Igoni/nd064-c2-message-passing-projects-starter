# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from app_folder.udaconnect import person_pb2 as person__pb2


class PersonServiceStub(object):
    """to retrieve individual and all persons
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/PersonService/Create',
                request_serializer=person__pb2.personmessage.SerializeToString,
                response_deserializer=person__pb2.personmessage.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/PersonService/Retrieve',
                request_serializer=person__pb2.PersonRequestMessage.SerializeToString,
                response_deserializer=person__pb2.personmessage.FromString,
                )
        self.RetrieveAll = channel.unary_unary(
                '/PersonService/RetrieveAll',
                request_serializer=person__pb2.PersonRequestMessage.SerializeToString,
                response_deserializer=person__pb2.PersonListMessage.FromString,
                )


class PersonServiceServicer(object):
    """to retrieve individual and all persons
    """

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PersonServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=person__pb2.personmessage.FromString,
                    response_serializer=person__pb2.personmessage.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=person__pb2.PersonRequestMessage.FromString,
                    response_serializer=person__pb2.personmessage.SerializeToString,
            ),
            'RetrieveAll': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveAll,
                    request_deserializer=person__pb2.PersonRequestMessage.FromString,
                    response_serializer=person__pb2.PersonListMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PersonService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PersonService(object):
    """to retrieve individual and all persons
    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PersonService/Create',
            person__pb2.personmessage.SerializeToString,
            person__pb2.personmessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PersonService/Retrieve',
            person__pb2.PersonRequestMessage.SerializeToString,
            person__pb2.personmessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PersonService/RetrieveAll',
            person__pb2.PersonRequestMessage.SerializeToString,
            person__pb2.PersonListMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
