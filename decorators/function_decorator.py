import functools


def cached(func):
    cached_args = {}

    @functools.wraps(func)
    def cached_func(*args):
        try:
            return cached_args[args]
        except KeyError:
            cached_args[args] = ret = func(*args)
            return ret

    return cached_func


@cached
def compute(x: int) -> int:
    print(f"Called with {x}")
    return x * x


def main() -> int:
    """
    >>> compute.__name__
    'compute'
    >>> compute.__annotations__
    {'x': <class 'int'>, 'return': <class 'int'>}
    """
    return 0


if __name__ == "__main__":
    exit(main())
