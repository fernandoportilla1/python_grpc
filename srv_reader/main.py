import grpc
import sales_records_pb2
import sales_records_pb2_grpc

from repositories.file_repository import FileRepository


def main():
    file_repository = FileRepository('/tmp/data/100_sr.json')
    data_readed = file_repository.read_data()

    for row in data_readed:
        with grpc.insecure_channel('srv_persistor:50051') as channel:
            stub = sales_records_pb2_grpc.SalesRecordStub(channel)
            req = sales_records_pb2.EmptyMessage()
            res = stub.PingSalesRecord(req)
            print(f'GRPC Recived: {res.ack} {row.get("producto")}')


if __name__ == '__main__':
    main()
