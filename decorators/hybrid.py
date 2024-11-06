import functools


def cached_func(maxsize):
    def cached_decorator(func):
        cached_data = {}

        @functools.wraps(func)
        def cached_dec(*args):
            try:
                return cached_data[args]
            except KeyError:
                cached_data[args] = ret = func(*args)
                return ret

        return cached_dec

    return cached_decorator


class cached_cls:
    def __init__(self, func, maxsize):
        self.func = func
        self.maxsize = maxsize
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


def cached(maxsize):
    def cached_decorator(func):
        return cached_cls(func, maxsize)

    return cached_decorator


@cached(maxsize=2)
def compute(x: int) -> int:
    """efficient compute function, caching upto `maxsize` results

    >>> compute.__name__
    'compute'

    >>> compute.__annotations__
    {'x': <class 'int'>, 'return': <class 'int'>}

    >>> "efficient compute function" in compute.__doc__
    True

    >>> compute        # doctest: +ELLIPSIS
    <function compute at ...>

    >>> compute(2)
    Calling with 2
    4

    >>> compute(3)
    Calling with 3
    9

    >>> compute(2)
    4
    """
    print(f"Calling with {x}")
    return x * x
