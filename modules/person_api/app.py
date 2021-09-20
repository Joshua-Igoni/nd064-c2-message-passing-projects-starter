from concurrent import futures

import grpc

import person_pb2_grpc
from grpc_service import PersonServicer



def grpc_serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(), server)
    server.add_insecure_port("[::]:4000")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    grpc_serve()
