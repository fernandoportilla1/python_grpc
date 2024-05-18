import grpc
import sales_records_pb2
import sales_records_pb2_grpc
from concurrent import futures


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sales_records_pb2_grpc.add_SalesRecordServicer_to_server(
        sales_records_pb2_grpc.SalesRecord(), server)

    server.add_insecure_port('[::]:50051')
    server.start()

    print("GPRC Persistor Server Working on 50051...")
    server.wait_for_termination()


if __name__ == '__main__':
    main()
