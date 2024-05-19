import os
import grpc
import sales_record_pb2
import sales_record_pb2_grpc

from repositories.file_repository import FileRepository


def main():
    file_repository = FileRepository('/tmp/data/100_sr.json')
    data_readed = file_repository.read_data()

    source = os.environ.get('HOSTNAME')

    for row in data_readed:
        with grpc.insecure_channel('srv_persistor:50051') as channel:
            stub = sales_record_pb2_grpc.SalesRecordStub(channel)
            req = sales_record_pb2.SalesRecordRequest(
                producto=row.get("producto"), cantidad=row.get("cantidad"), precio=row.get("precio"))
            res = stub.SendSalesRecords(req)
            print(f'GRPC Recived: {res} {row.get("producto")}')


if __name__ == '__main__':
    main()
