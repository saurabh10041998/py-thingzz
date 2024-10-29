from typing import Union
from typing import overload
from typing import Protocol

class Indexable(Protocol):
    def __index__(self) -> int: ...

@overload
def bytes_getitem(b: bytes, idx: Indexable) -> int: ...

@overload
def bytes_getitem(b: bytes, idx: slice) -> bytes: ...

def bytes_getitem(
    b: bytes,
    idx: Union[Indexable, slice]
) -> Union[int, bytes]:
    return b[idx]


foo = b'1000'
print(bytes_getitem(foo, 0) - ord('0'))


class C:
    def __index__(self) -> int:
        return 3

print(bytes_getitem(foo, C()))
