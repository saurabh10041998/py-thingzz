from dataclasses import dataclass
from typing import Literal
from typing import Set

@dataclass
class Error:
    error_code: Literal[1, 2, 3, 4, 5]
    disposed_of: bool


@dataclass
class Snack:
    name: Literal["Hot Dog", "Pretzel"]
    condiments: Set[Literal["Mustard", "Ketchup"]]


# following things will not type check
Error(0, False)
Snack("Not valid", set())
Snack("Pretzel", {"Mustard", "Relish"})
