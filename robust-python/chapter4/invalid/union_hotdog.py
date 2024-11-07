from typing import Union


class HotDog:
    pass


class Pretzel:
    pass


def dispense_hot_dog() -> HotDog:
    return HotDog()


def dispense_pretzel() -> Pretzel:
    return Pretzel()


def dispense_snack(user_input: str) -> Union[HotDog, Pretzel]:
    """factory method to dispense the snacks based on user input

    >>> assert isinstance(dispense_snack('Hot Dog'), HotDog)

    >>> assert isinstance(dispense_snack('Pretzel'), Pretzel)

    >>> import pytest
    >>> with pytest.raises(RuntimeError) as excinfo:
    ...     dispense_snack('Samosa')

    >>> 'Samosa' in excinfo.value.args[0]
    True
    """
    if user_input == "Hot Dog":
        return dispense_hot_dog()

    elif user_input == "Pretzel":
        return dispense_pretzel()

    raise RuntimeError(
        "Should never reach this part of code, as invalid"
       f" user input detected: {user_input=!r}"
    )
