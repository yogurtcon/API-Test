# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mods/misc/rpcMessage.ext.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mods/misc/rpcMessage.ext.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'\242\002\005PROTO',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1emods/misc/rpcMessage.ext.proto\x12\x02pb\"\x82\x01\n\x08RPCInput\x12\x0b\n\x03obj\x18\x01 \x01(\t\x12\x0c\n\x04\x66unc\x18\x02 \x01(\t\x12\x0b\n\x03req\x18\x03 \x01(\x0c\x12\"\n\x03opt\x18\x04 \x03(\x0b\x32\x15.pb.RPCInput.OptEntry\x1a*\n\x08OptEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9f\x01\n\tRPCOutput\x12\x0b\n\x03ret\x18\x01 \x01(\x05\x12\x0b\n\x03rsp\x18\x02 \x01(\x0c\x12#\n\x03opt\x18\x03 \x03(\x0b\x32\x16.pb.RPCOutput.OptEntry\x12\x0c\n\x04\x64\x65sc\x18\x04 \x01(\t\x12\x0b\n\x03obj\x18\x05 \x01(\t\x12\x0c\n\x04\x66unc\x18\x06 \x01(\t\x1a*\n\x08OptEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x08\xa2\x02\x05PROTOb\x06proto3'
)




_RPCINPUT_OPTENTRY = _descriptor.Descriptor(
  name='OptEntry',
  full_name='pb.RPCInput.OptEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pb.RPCInput.OptEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='pb.RPCInput.OptEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=169,
)

_RPCINPUT = _descriptor.Descriptor(
  name='RPCInput',
  full_name='pb.RPCInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='obj', full_name='pb.RPCInput.obj', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='func', full_name='pb.RPCInput.func', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='req', full_name='pb.RPCInput.req', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opt', full_name='pb.RPCInput.opt', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RPCINPUT_OPTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=169,
)


_RPCOUTPUT_OPTENTRY = _descriptor.Descriptor(
  name='OptEntry',
  full_name='pb.RPCOutput.OptEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pb.RPCOutput.OptEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='pb.RPCOutput.OptEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=169,
)

_RPCOUTPUT = _descriptor.Descriptor(
  name='RPCOutput',
  full_name='pb.RPCOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='pb.RPCOutput.ret', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rsp', full_name='pb.RPCOutput.rsp', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opt', full_name='pb.RPCOutput.opt', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desc', full_name='pb.RPCOutput.desc', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='obj', full_name='pb.RPCOutput.obj', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='func', full_name='pb.RPCOutput.func', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RPCOUTPUT_OPTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=331,
)

_RPCINPUT_OPTENTRY.containing_type = _RPCINPUT
_RPCINPUT.fields_by_name['opt'].message_type = _RPCINPUT_OPTENTRY
_RPCOUTPUT_OPTENTRY.containing_type = _RPCOUTPUT
_RPCOUTPUT.fields_by_name['opt'].message_type = _RPCOUTPUT_OPTENTRY
DESCRIPTOR.message_types_by_name['RPCInput'] = _RPCINPUT
DESCRIPTOR.message_types_by_name['RPCOutput'] = _RPCOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RPCInput = _reflection.GeneratedProtocolMessageType('RPCInput', (_message.Message,), {

  'OptEntry' : _reflection.GeneratedProtocolMessageType('OptEntry', (_message.Message,), {
    'DESCRIPTOR' : _RPCINPUT_OPTENTRY,
    '__module__' : 'mods.misc.rpcMessage.ext_pb2'
    # @@protoc_insertion_point(class_scope:pb.RPCInput.OptEntry)
    })
  ,
  'DESCRIPTOR' : _RPCINPUT,
  '__module__' : 'mods.misc.rpcMessage.ext_pb2'
  # @@protoc_insertion_point(class_scope:pb.RPCInput)
  })
_sym_db.RegisterMessage(RPCInput)
_sym_db.RegisterMessage(RPCInput.OptEntry)

RPCOutput = _reflection.GeneratedProtocolMessageType('RPCOutput', (_message.Message,), {

  'OptEntry' : _reflection.GeneratedProtocolMessageType('OptEntry', (_message.Message,), {
    'DESCRIPTOR' : _RPCOUTPUT_OPTENTRY,
    '__module__' : 'mods.misc.rpcMessage.ext_pb2'
    # @@protoc_insertion_point(class_scope:pb.RPCOutput.OptEntry)
    })
  ,
  'DESCRIPTOR' : _RPCOUTPUT,
  '__module__' : 'mods.misc.rpcMessage.ext_pb2'
  # @@protoc_insertion_point(class_scope:pb.RPCOutput)
  })
_sym_db.RegisterMessage(RPCOutput)
_sym_db.RegisterMessage(RPCOutput.OptEntry)


DESCRIPTOR._options = None
_RPCINPUT_OPTENTRY._options = None
_RPCOUTPUT_OPTENTRY._options = None
# @@protoc_insertion_point(module_scope)
