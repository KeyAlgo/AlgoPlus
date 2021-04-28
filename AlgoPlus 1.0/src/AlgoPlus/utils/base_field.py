# encoding:utf-8

# AlgoPlus量化投资开源框架
# 微信公众号：AlgoPlus
# 官网：http://algo.plus

from ctypes import *


def to_bytes(value):
    return value if isinstance(value, bytes) else str(value).encode(encoding='utf-8')

def to_str(value):
    return value.decode(encoding='gb18030', errors='ignore') if isinstance(value, bytes) else str(value)


class BaseField(Structure):
    def to_dict(self):
        result = {}
        for key, _ in self._fields_:
            _value = getattr(self, key)
            result[key] = _value
        return result

    def to_str_dict(self):
        result = {}
        for key, _ in self._fields_:
            _value = getattr(self, key)
            if isinstance(_value, bytes):
                result[key] = to_str(_value)
            else:
                result[key] = _value
        return result

    def to_list(self):
        result = []
        for key, _ in self._fields_:
            _value = getattr(self, key)
            result.append(_value)
        return result

    def to_str_list(self):
        result = []
        for key, _ in self._fields_:
            _value = getattr(self, key)
            if isinstance(_value, bytes):
                result.append(to_str(_value))
            else:
                result.append(_value)
        return result

    def __repr__(self):
        return f'{self.__class__.__name__}->{self.to_str_dict()}'

    @classmethod
    def get_key_field_list(cls):
        key_field_list = []
        for field_name, _ in cls._fields_:
            key_field_list.append(field_name)
        return key_field_list
