# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sales_record.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12sales_record.proto\"\x0e\n\x0c\x45mptyMessage\"&\n\x17SalesRecordPingResponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\t\"#\n\x13SalesRecordResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"H\n\x12SalesRecordRequest\x12\x10\n\x08producto\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61ntidad\x18\x02 \x01(\x01\x12\x0e\n\x06precio\x18\x03 \x01(\x01\x32\x89\x01\n\x0bSalesRecord\x12;\n\x10PingSalesRecords\x12\r.EmptyMessage\x1a\x18.SalesRecordPingResponse\x12=\n\x10SendSalesRecords\x12\x13.SalesRecordRequest\x1a\x14.SalesRecordResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sales_record_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTYMESSAGE']._serialized_start=22
  _globals['_EMPTYMESSAGE']._serialized_end=36
  _globals['_SALESRECORDPINGRESPONSE']._serialized_start=38
  _globals['_SALESRECORDPINGRESPONSE']._serialized_end=76
  _globals['_SALESRECORDRESPONSE']._serialized_start=78
  _globals['_SALESRECORDRESPONSE']._serialized_end=113
  _globals['_SALESRECORDREQUEST']._serialized_start=115
  _globals['_SALESRECORDREQUEST']._serialized_end=187
  _globals['_SALESRECORD']._serialized_start=190
  _globals['_SALESRECORD']._serialized_end=327
# @@protoc_insertion_point(module_scope)