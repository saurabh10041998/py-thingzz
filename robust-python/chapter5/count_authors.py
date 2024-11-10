from collections import defaultdict
from dataclasses import dataclass
from typing import List
from typing import Dict


@dataclass
class Cookbook:
    author: str


def create_author_count_mapping(
    cookbooks: List[Cookbook]
) -> Dict[str, int]:
    counter: Dict[str, int] = defaultdict(lambda: 0)
    for cookbook in cookbooks:
        counter[cookbook.author] += 1
    return counter



def test_count_author():
    assert {'Pat Viafore': 2, 'J Kenny Wahlberg': 1} \
            == create_author_count_mapping(
                [
                    Cookbook('Pat Viafore'),
                    Cookbook('Pat Viafore'),
                    Cookbook('J Kenny Wahlberg'),
                ]
            )
