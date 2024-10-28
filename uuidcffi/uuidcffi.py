import uuid
import _uuidcffi

_lib = _uuidcffi.lib
_ffi = _uuidcffi.ffi

def uuid_generate() -> uuid.UUID:
    buf = _ffi.new("uuid_t")
    _lib.uuid_generate(buf)
    return uuid.UUID(bytes=bytes(buf))
