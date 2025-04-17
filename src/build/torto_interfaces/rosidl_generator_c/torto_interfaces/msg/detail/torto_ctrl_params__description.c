// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from torto_interfaces:msg/TortoCtrlParams.idl
// generated code does not contain a copyright notice

#include "torto_interfaces/msg/detail/torto_ctrl_params__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_torto_interfaces
const rosidl_type_hash_t *
torto_interfaces__msg__TortoCtrlParams__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x0a, 0x86, 0x8c, 0xea, 0x2c, 0x66, 0xf6, 0xae,
      0x54, 0xa6, 0x33, 0x94, 0xed, 0x18, 0xb7, 0xb3,
      0x66, 0xee, 0xff, 0xb3, 0xcb, 0x8d, 0x1e, 0x21,
      0xc3, 0x4d, 0xcb, 0xf2, 0xcf, 0x3a, 0x4a, 0x3d,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char torto_interfaces__msg__TortoCtrlParams__TYPE_NAME[] = "torto_interfaces/msg/TortoCtrlParams";

// Define type names, field names, and default values
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__vx[] = "vx";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__vy[] = "vy";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__vz[] = "vz";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__vangular[] = "vangular";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__angle_fr[] = "angle_fr";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__angle_fl[] = "angle_fl";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__angle_br[] = "angle_br";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__angle_bl[] = "angle_bl";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__step_offset[] = "step_offset";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__step_period[] = "step_period";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__gait_offset_fr[] = "gait_offset_fr";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__gait_offset_fl[] = "gait_offset_fl";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__gait_offset_br[] = "gait_offset_br";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__gait_offset_bl[] = "gait_offset_bl";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__body_position_x[] = "body_position_x";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__body_position_y[] = "body_position_y";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__body_position_z[] = "body_position_z";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__body_orientation_roll[] = "body_orientation_roll";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__body_orientation_pitch[] = "body_orientation_pitch";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__body_orientation_yawn[] = "body_orientation_yawn";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_fr_x[] = "foot_position_fr_x";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_fr_y[] = "foot_position_fr_y";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_fr_z[] = "foot_position_fr_z";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_fl_x[] = "foot_position_fl_x";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_fl_y[] = "foot_position_fl_y";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_fl_z[] = "foot_position_fl_z";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_br_x[] = "foot_position_br_x";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_br_y[] = "foot_position_br_y";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_br_z[] = "foot_position_br_z";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_bl_x[] = "foot_position_bl_x";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_bl_y[] = "foot_position_bl_y";
static char torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_bl_z[] = "foot_position_bl_z";

static rosidl_runtime_c__type_description__Field torto_interfaces__msg__TortoCtrlParams__FIELDS[] = {
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__vx, 2, 2},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__vy, 2, 2},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__vz, 2, 2},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__vangular, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__angle_fr, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__angle_fl, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__angle_br, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__angle_bl, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__step_offset, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__step_period, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__gait_offset_fr, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__gait_offset_fl, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__gait_offset_br, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__gait_offset_bl, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__body_position_x, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__body_position_y, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__body_position_z, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__body_orientation_roll, 21, 21},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__body_orientation_pitch, 22, 22},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__body_orientation_yawn, 21, 21},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_fr_x, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_fr_y, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_fr_z, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_fl_x, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_fl_y, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_fl_z, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_br_x, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_br_y, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_br_z, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_bl_x, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_bl_y, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoCtrlParams__FIELD_NAME__foot_position_bl_z, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
torto_interfaces__msg__TortoCtrlParams__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {torto_interfaces__msg__TortoCtrlParams__TYPE_NAME, 36, 36},
      {torto_interfaces__msg__TortoCtrlParams__FIELDS, 32, 32},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 vx\n"
  "float64 vy\n"
  "float64 vz\n"
  "float64 vangular\n"
  "float64 angle_fr\n"
  "float64 angle_fl\n"
  "float64 angle_br\n"
  "float64 angle_bl\n"
  "float64 step_offset\n"
  "float64 step_period\n"
  "float64 gait_offset_fr\n"
  "float64 gait_offset_fl\n"
  "float64 gait_offset_br\n"
  "float64 gait_offset_bl\n"
  "float64 body_position_x\n"
  "float64 body_position_y\n"
  "float64 body_position_z\n"
  "float64 body_orientation_roll\n"
  "float64 body_orientation_pitch\n"
  "float64 body_orientation_yawn\n"
  "float64 foot_position_fr_x \n"
  "float64 foot_position_fr_y\n"
  "float64 foot_position_fr_z \n"
  "float64 foot_position_fl_x \n"
  "float64 foot_position_fl_y\n"
  "float64 foot_position_fl_z \n"
  "float64 foot_position_br_x \n"
  "float64 foot_position_br_y\n"
  "float64 foot_position_br_z \n"
  "float64 foot_position_bl_x \n"
  "float64 foot_position_bl_y\n"
  "float64 foot_position_bl_z ";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
torto_interfaces__msg__TortoCtrlParams__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {torto_interfaces__msg__TortoCtrlParams__TYPE_NAME, 36, 36},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 744, 744},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
torto_interfaces__msg__TortoCtrlParams__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *torto_interfaces__msg__TortoCtrlParams__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
