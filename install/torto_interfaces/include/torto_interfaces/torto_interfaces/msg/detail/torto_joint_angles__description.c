// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from torto_interfaces:msg/TortoJointAngles.idl
// generated code does not contain a copyright notice

#include "torto_interfaces/msg/detail/torto_joint_angles__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_torto_interfaces
const rosidl_type_hash_t *
torto_interfaces__msg__TortoJointAngles__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xd5, 0x7f, 0xbd, 0x95, 0x50, 0x96, 0xe2, 0xc5,
      0xcf, 0x03, 0x26, 0xdb, 0x03, 0xfb, 0xe1, 0xec,
      0x51, 0xe8, 0xc2, 0xa0, 0x97, 0xe7, 0x97, 0x88,
      0xc9, 0xc4, 0x3c, 0xb9, 0xad, 0x9a, 0x86, 0xa7,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char torto_interfaces__msg__TortoJointAngles__TYPE_NAME[] = "torto_interfaces/msg/TortoJointAngles";

// Define type names, field names, and default values
static char torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_fr_detoid[] = "theta_deg_fr_detoid";
static char torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_fr_femur[] = "theta_deg_fr_femur";
static char torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_fr_tibia[] = "theta_deg_fr_tibia";
static char torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_fl_detoid[] = "theta_deg_fl_detoid";
static char torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_fl_femur[] = "theta_deg_fl_femur";
static char torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_fl_tibia[] = "theta_deg_fl_tibia";
static char torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_br_detoid[] = "theta_deg_br_detoid";
static char torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_br_femur[] = "theta_deg_br_femur";
static char torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_br_tibia[] = "theta_deg_br_tibia";
static char torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_bl_detoid[] = "theta_deg_bl_detoid";
static char torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_bl_femur[] = "theta_deg_bl_femur";
static char torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_bl_tibia[] = "theta_deg_bl_tibia";

static rosidl_runtime_c__type_description__Field torto_interfaces__msg__TortoJointAngles__FIELDS[] = {
  {
    {torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_fr_detoid, 19, 19},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_fr_femur, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_fr_tibia, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_fl_detoid, 19, 19},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_fl_femur, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_fl_tibia, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_br_detoid, 19, 19},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_br_femur, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_br_tibia, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_bl_detoid, 19, 19},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_bl_femur, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {torto_interfaces__msg__TortoJointAngles__FIELD_NAME__theta_deg_bl_tibia, 18, 18},
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
torto_interfaces__msg__TortoJointAngles__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {torto_interfaces__msg__TortoJointAngles__TYPE_NAME, 37, 37},
      {torto_interfaces__msg__TortoJointAngles__FIELDS, 12, 12},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 theta_deg_fr_detoid\n"
  "float64 theta_deg_fr_femur\n"
  "float64 theta_deg_fr_tibia\n"
  "float64 theta_deg_fl_detoid\n"
  "float64 theta_deg_fl_femur\n"
  "float64 theta_deg_fl_tibia\n"
  "float64 theta_deg_br_detoid\n"
  "float64 theta_deg_br_femur\n"
  "float64 theta_deg_br_tibia\n"
  "float64 theta_deg_bl_detoid\n"
  "float64 theta_deg_bl_femur\n"
  "float64 theta_deg_bl_tibia";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
torto_interfaces__msg__TortoJointAngles__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {torto_interfaces__msg__TortoJointAngles__TYPE_NAME, 37, 37},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 327, 327},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
torto_interfaces__msg__TortoJointAngles__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *torto_interfaces__msg__TortoJointAngles__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
