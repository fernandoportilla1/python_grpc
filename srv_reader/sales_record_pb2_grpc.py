# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import sales_record_pb2 as sales__record__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in sales_record_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class SalesRecordStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PingSalesRecords = channel.unary_unary(
                '/SalesRecord/PingSalesRecords',
                request_serializer=sales__record__pb2.EmptyMessage.SerializeToString,
                response_deserializer=sales__record__pb2.SalesRecordPingResponse.FromString,
                _registered_method=True)
        self.SendSalesRecords = channel.unary_unary(
                '/SalesRecord/SendSalesRecords',
                request_serializer=sales__record__pb2.SalesRecordRequest.SerializeToString,
                response_deserializer=sales__record__pb2.SalesRecordResponse.FromString,
                _registered_method=True)


class SalesRecordServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PingSalesRecords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendSalesRecords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SalesRecordServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PingSalesRecords': grpc.unary_unary_rpc_method_handler(
                    servicer.PingSalesRecords,
                    request_deserializer=sales__record__pb2.EmptyMessage.FromString,
                    response_serializer=sales__record__pb2.SalesRecordPingResponse.SerializeToString,
            ),
            'SendSalesRecords': grpc.unary_unary_rpc_method_handler(
                    servicer.SendSalesRecords,
                    request_deserializer=sales__record__pb2.SalesRecordRequest.FromString,
                    response_serializer=sales__record__pb2.SalesRecordResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SalesRecord', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SalesRecord(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PingSalesRecords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/SalesRecord/PingSalesRecords',
            sales__record__pb2.EmptyMessage.SerializeToString,
            sales__record__pb2.SalesRecordPingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SendSalesRecords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/SalesRecord/SendSalesRecords',
            sales__record__pb2.SalesRecordRequest.SerializeToString,
            sales__record__pb2.SalesRecordResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
