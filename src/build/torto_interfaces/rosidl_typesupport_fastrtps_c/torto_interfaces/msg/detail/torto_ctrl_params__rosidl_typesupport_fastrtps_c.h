// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from torto_interfaces:msg/TortoCtrlParams.idl
// generated code does not contain a copyright notice
#ifndef TORTO_INTERFACES__MSG__DETAIL__TORTO_CTRL_PARAMS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define TORTO_INTERFACES__MSG__DETAIL__TORTO_CTRL_PARAMS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "torto_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "torto_interfaces/msg/detail/torto_ctrl_params__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_torto_interfaces
bool cdr_serialize_torto_interfaces__msg__TortoCtrlParams(
  const torto_interfaces__msg__TortoCtrlParams * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_torto_interfaces
bool cdr_deserialize_torto_interfaces__msg__TortoCtrlParams(
  eprosima::fastcdr::Cdr &,
  torto_interfaces__msg__TortoCtrlParams * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_torto_interfaces
size_t get_serialized_size_torto_interfaces__msg__TortoCtrlParams(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_torto_interfaces
size_t max_serialized_size_torto_interfaces__msg__TortoCtrlParams(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_torto_interfaces
bool cdr_serialize_key_torto_interfaces__msg__TortoCtrlParams(
  const torto_interfaces__msg__TortoCtrlParams * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_torto_interfaces
size_t get_serialized_size_key_torto_interfaces__msg__TortoCtrlParams(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_torto_interfaces
size_t max_serialized_size_key_torto_interfaces__msg__TortoCtrlParams(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_torto_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, torto_interfaces, msg, TortoCtrlParams)();

#ifdef __cplusplus
}
#endif

#endif  // TORTO_INTERFACES__MSG__DETAIL__TORTO_CTRL_PARAMS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
