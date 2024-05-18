import grpc
import sales_records_pb2
import sales_records_pb2_grpc
from concurrent import futures


def main():
    with grpc.insecure_channel('srv_persistor:50051') as channel:
        stub = sales_records_pb2_grpc.SalesRecordStub(channel)
        req = sales_records_pb2.EmptyMessage()
        res = stub.PingSalesRecord(req)
        print(f'GRPC Recived: {res.ack}')


if __name__ == '__main__':
    main()
