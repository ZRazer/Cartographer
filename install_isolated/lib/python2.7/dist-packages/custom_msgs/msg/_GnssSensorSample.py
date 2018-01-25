# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from custom_msgs/GnssSensorSample.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class GnssSensorSample(genpy.Message):
  _md5sum = "ae4c67b6a1b5c4f7d7a22900ef78225d"
  _type = "custom_msgs/GnssSensorSample"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# This is a message to hold data a GNSS unit
# Supported for MTi Devices with FW 1.4 and above.

std_msgs/Float64 itow
std_msgs/Float64 fix

float64 latitude
float64 longitude
float64 hEll
float64 hMsl

# ENU velocity
geometry_msgs/Vector3 vel

float64 hAcc
float64 vAcc
float64 sAcc

float64 pDop
float64 hDop
float64 vDop

float64 numSat
float64 heading
float64 headingAcc




================================================================================
MSG: std_msgs/Float64
float64 data
================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['itow','fix','latitude','longitude','hEll','hMsl','vel','hAcc','vAcc','sAcc','pDop','hDop','vDop','numSat','heading','headingAcc']
  _slot_types = ['std_msgs/Float64','std_msgs/Float64','float64','float64','float64','float64','geometry_msgs/Vector3','float64','float64','float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       itow,fix,latitude,longitude,hEll,hMsl,vel,hAcc,vAcc,sAcc,pDop,hDop,vDop,numSat,heading,headingAcc

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GnssSensorSample, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.itow is None:
        self.itow = std_msgs.msg.Float64()
      if self.fix is None:
        self.fix = std_msgs.msg.Float64()
      if self.latitude is None:
        self.latitude = 0.
      if self.longitude is None:
        self.longitude = 0.
      if self.hEll is None:
        self.hEll = 0.
      if self.hMsl is None:
        self.hMsl = 0.
      if self.vel is None:
        self.vel = geometry_msgs.msg.Vector3()
      if self.hAcc is None:
        self.hAcc = 0.
      if self.vAcc is None:
        self.vAcc = 0.
      if self.sAcc is None:
        self.sAcc = 0.
      if self.pDop is None:
        self.pDop = 0.
      if self.hDop is None:
        self.hDop = 0.
      if self.vDop is None:
        self.vDop = 0.
      if self.numSat is None:
        self.numSat = 0.
      if self.heading is None:
        self.heading = 0.
      if self.headingAcc is None:
        self.headingAcc = 0.
    else:
      self.itow = std_msgs.msg.Float64()
      self.fix = std_msgs.msg.Float64()
      self.latitude = 0.
      self.longitude = 0.
      self.hEll = 0.
      self.hMsl = 0.
      self.vel = geometry_msgs.msg.Vector3()
      self.hAcc = 0.
      self.vAcc = 0.
      self.sAcc = 0.
      self.pDop = 0.
      self.hDop = 0.
      self.vDop = 0.
      self.numSat = 0.
      self.heading = 0.
      self.headingAcc = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_18d().pack(_x.itow.data, _x.fix.data, _x.latitude, _x.longitude, _x.hEll, _x.hMsl, _x.vel.x, _x.vel.y, _x.vel.z, _x.hAcc, _x.vAcc, _x.sAcc, _x.pDop, _x.hDop, _x.vDop, _x.numSat, _x.heading, _x.headingAcc))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.itow is None:
        self.itow = std_msgs.msg.Float64()
      if self.fix is None:
        self.fix = std_msgs.msg.Float64()
      if self.vel is None:
        self.vel = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 144
      (_x.itow.data, _x.fix.data, _x.latitude, _x.longitude, _x.hEll, _x.hMsl, _x.vel.x, _x.vel.y, _x.vel.z, _x.hAcc, _x.vAcc, _x.sAcc, _x.pDop, _x.hDop, _x.vDop, _x.numSat, _x.heading, _x.headingAcc,) = _get_struct_18d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_18d().pack(_x.itow.data, _x.fix.data, _x.latitude, _x.longitude, _x.hEll, _x.hMsl, _x.vel.x, _x.vel.y, _x.vel.z, _x.hAcc, _x.vAcc, _x.sAcc, _x.pDop, _x.hDop, _x.vDop, _x.numSat, _x.heading, _x.headingAcc))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.itow is None:
        self.itow = std_msgs.msg.Float64()
      if self.fix is None:
        self.fix = std_msgs.msg.Float64()
      if self.vel is None:
        self.vel = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 144
      (_x.itow.data, _x.fix.data, _x.latitude, _x.longitude, _x.hEll, _x.hMsl, _x.vel.x, _x.vel.y, _x.vel.z, _x.hAcc, _x.vAcc, _x.sAcc, _x.pDop, _x.hDop, _x.vDop, _x.numSat, _x.heading, _x.headingAcc,) = _get_struct_18d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_18d = None
def _get_struct_18d():
    global _struct_18d
    if _struct_18d is None:
        _struct_18d = struct.Struct("<18d")
    return _struct_18d
