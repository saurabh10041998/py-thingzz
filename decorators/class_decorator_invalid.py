class cached:
    def __init__(self, func):
        self.func = func
        self.cached_data = {}

    def __call__(self, *args):
        try:
            return self.cached_data[args]
        except KeyError:
            self.cached_data[args] = ret = self.func(*args)
            return  ret


@cached
def compute(x: int) -> int:
    print(f"Called with {x}")
    return x * x

def main() -> int:
    """only doctests that will pass
    >>> compute(2)
    Called with 2
    4

    >>> compute(2)
    4
    """
    return 0

if __name__ == "__main__":
    exit(main())


