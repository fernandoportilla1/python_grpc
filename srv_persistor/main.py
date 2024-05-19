import grpc
import sales_record_pb2
import sales_record_pb2_grpc
from concurrent import futures


class SalesRecord(sales_record_pb2_grpc.SalesRecordServicer):
    def PingSalesRecords(self, request, context):
        response = sales_record_pb2.SalesRecordPingResponse(ack='1')
        return response

    def SendSalesRecords(self, request, context):
        return sales_record_pb2.SalesRecordResponse(data=request.producto)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sales_record_pb2_grpc.add_SalesRecordServicer_to_server(
        SalesRecord(), server)

    server.add_insecure_port('[::]:50051')
    server.start()

    print("GPRC Persistor Server Working on 50051...")
    server.wait_for_termination()


if __name__ == '__main__':
    main()
