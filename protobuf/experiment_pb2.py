# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experiment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import optimizers_pb2 as optimizers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='experiment.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x65xperiment.proto\x1a\x10optimizers.proto\"M\n\x05Layer\x12\x17\n\x0finput_dimension\x18\x01 \x01(\x05\x12\x18\n\x10output_dimension\x18\x02 \x01(\x05\"\x11\n\x04Type\x12\t\n\x05\x44\x45NSE\x10\x00\"B\n\x05\x45poch\x12\x13\n\x0bnum_seconds\x18\x01 \x01(\x02\x12\x0c\n\x04loss\x18\x02 \x01(\x02\x12\x16\n\x0etrain_accuracy\x18\x03 \x01(\x02\"\x88\x03\n\nExperiment\x12\x12\n\nbatch_size\x18\x01 \x01(\x05\x12\x15\n\rlearning_rate\x18\x02 \x01(\x02\x12\x17\n\x0fstart_date_time\x18\x03 \x01(\t\x12\x15\n\rend_date_time\x18\x04 \x01(\t\x12\x19\n\tstructure\x18\x05 \x03(\x0b\x32\x06.Layer\x12\x17\n\x07results\x18\x06 \x03(\x0b\x32\x06.Epoch\x12\x13\n\x03sgd\x18\x07 \x01(\x0b\x32\x04.SGDH\x00\x12\x1b\n\x07rmsprop\x18\x08 \x01(\x0b\x32\x08.RMSpropH\x00\x12\x1b\n\x07\x61\x64\x61grad\x18\t \x01(\x0b\x32\x08.AdagradH\x00\x12\x1d\n\x08\x61\x64\x61\x64\x65lta\x18\n \x01(\x0b\x32\t.AdadeltaH\x00\x12\x15\n\x04\x61\x64\x61m\x18\x0b \x01(\x0b\x32\x05.AdamH\x00\x12\x19\n\x06\x61\x64\x61max\x18\x0c \x01(\x0b\x32\x07.AdamaxH\x00\x12\x13\n\x0b\x64\x65scription\x18\r \x01(\t\")\n\x07\x44\x61taset\x12\r\n\tOSU_TTBAR\x10\x00\x12\x0f\n\x0bOSU_TTHIGGS\x10\x01\x42\x0b\n\toptimizerb\x06proto3')
  ,
  dependencies=[optimizers__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_LAYER_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Layer.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DENSE', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=98,
  serialized_end=115,
)
_sym_db.RegisterEnumDescriptor(_LAYER_TYPE)

_EXPERIMENT_DATASET = _descriptor.EnumDescriptor(
  name='Dataset',
  full_name='Experiment.Dataset',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OSU_TTBAR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OSU_TTHIGGS', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=524,
  serialized_end=565,
)
_sym_db.RegisterEnumDescriptor(_EXPERIMENT_DATASET)


_LAYER = _descriptor.Descriptor(
  name='Layer',
  full_name='Layer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_dimension', full_name='Layer.input_dimension', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_dimension', full_name='Layer.output_dimension', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LAYER_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=115,
)


_EPOCH = _descriptor.Descriptor(
  name='Epoch',
  full_name='Epoch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_seconds', full_name='Epoch.num_seconds', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loss', full_name='Epoch.loss', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='train_accuracy', full_name='Epoch.train_accuracy', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=183,
)


_EXPERIMENT = _descriptor.Descriptor(
  name='Experiment',
  full_name='Experiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='Experiment.batch_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='Experiment.learning_rate', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_date_time', full_name='Experiment.start_date_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_date_time', full_name='Experiment.end_date_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='structure', full_name='Experiment.structure', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='results', full_name='Experiment.results', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sgd', full_name='Experiment.sgd', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rmsprop', full_name='Experiment.rmsprop', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adagrad', full_name='Experiment.adagrad', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adadelta', full_name='Experiment.adadelta', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adam', full_name='Experiment.adam', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adamax', full_name='Experiment.adamax', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='Experiment.description', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXPERIMENT_DATASET,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='optimizer', full_name='Experiment.optimizer',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=186,
  serialized_end=578,
)

_LAYER_TYPE.containing_type = _LAYER
_EXPERIMENT.fields_by_name['structure'].message_type = _LAYER
_EXPERIMENT.fields_by_name['results'].message_type = _EPOCH
_EXPERIMENT.fields_by_name['sgd'].message_type = optimizers__pb2._SGD
_EXPERIMENT.fields_by_name['rmsprop'].message_type = optimizers__pb2._RMSPROP
_EXPERIMENT.fields_by_name['adagrad'].message_type = optimizers__pb2._ADAGRAD
_EXPERIMENT.fields_by_name['adadelta'].message_type = optimizers__pb2._ADADELTA
_EXPERIMENT.fields_by_name['adam'].message_type = optimizers__pb2._ADAM
_EXPERIMENT.fields_by_name['adamax'].message_type = optimizers__pb2._ADAMAX
_EXPERIMENT_DATASET.containing_type = _EXPERIMENT
_EXPERIMENT.oneofs_by_name['optimizer'].fields.append(
  _EXPERIMENT.fields_by_name['sgd'])
_EXPERIMENT.fields_by_name['sgd'].containing_oneof = _EXPERIMENT.oneofs_by_name['optimizer']
_EXPERIMENT.oneofs_by_name['optimizer'].fields.append(
  _EXPERIMENT.fields_by_name['rmsprop'])
_EXPERIMENT.fields_by_name['rmsprop'].containing_oneof = _EXPERIMENT.oneofs_by_name['optimizer']
_EXPERIMENT.oneofs_by_name['optimizer'].fields.append(
  _EXPERIMENT.fields_by_name['adagrad'])
_EXPERIMENT.fields_by_name['adagrad'].containing_oneof = _EXPERIMENT.oneofs_by_name['optimizer']
_EXPERIMENT.oneofs_by_name['optimizer'].fields.append(
  _EXPERIMENT.fields_by_name['adadelta'])
_EXPERIMENT.fields_by_name['adadelta'].containing_oneof = _EXPERIMENT.oneofs_by_name['optimizer']
_EXPERIMENT.oneofs_by_name['optimizer'].fields.append(
  _EXPERIMENT.fields_by_name['adam'])
_EXPERIMENT.fields_by_name['adam'].containing_oneof = _EXPERIMENT.oneofs_by_name['optimizer']
_EXPERIMENT.oneofs_by_name['optimizer'].fields.append(
  _EXPERIMENT.fields_by_name['adamax'])
_EXPERIMENT.fields_by_name['adamax'].containing_oneof = _EXPERIMENT.oneofs_by_name['optimizer']
DESCRIPTOR.message_types_by_name['Layer'] = _LAYER
DESCRIPTOR.message_types_by_name['Epoch'] = _EPOCH
DESCRIPTOR.message_types_by_name['Experiment'] = _EXPERIMENT

Layer = _reflection.GeneratedProtocolMessageType('Layer', (_message.Message,), dict(
  DESCRIPTOR = _LAYER,
  __module__ = 'experiment_pb2'
  # @@protoc_insertion_point(class_scope:Layer)
  ))
_sym_db.RegisterMessage(Layer)

Epoch = _reflection.GeneratedProtocolMessageType('Epoch', (_message.Message,), dict(
  DESCRIPTOR = _EPOCH,
  __module__ = 'experiment_pb2'
  # @@protoc_insertion_point(class_scope:Epoch)
  ))
_sym_db.RegisterMessage(Epoch)

Experiment = _reflection.GeneratedProtocolMessageType('Experiment', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENT,
  __module__ = 'experiment_pb2'
  # @@protoc_insertion_point(class_scope:Experiment)
  ))
_sym_db.RegisterMessage(Experiment)


# @@protoc_insertion_point(module_scope)