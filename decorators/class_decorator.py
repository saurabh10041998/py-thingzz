import functools


class cached:
    def __init__(self, func):
        self.func = func
        self.cached_data = {}
        functools.update_wrapper(self, func)

    def __call__(self, *args):
        try:
            return self.cached_data[args]
        except KeyError:
            self.cached_data[args] = ret = self.func(*args)
            return ret

    def __repr__(self):
        return repr(self.func)


@cached
def compute(x: int) -> int:
    """doctest retaining all the dunders
    >>> compute.__name__
    'compute'

    >>> compute.__annotations__
    {'x': <class 'int'>, 'return': <class 'int'>}

    >>> 'doctest retaining' in compute.__doc__
    True

    >>> compute     # doctest: +ELLIPSIS
    <function compute at ...>

    >>> compute(2)
    Calling with 2
    4

    >>> compute(2)
    4
    """
    print(f"Calling with {x}")
    return x * x
