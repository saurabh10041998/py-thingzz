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


def test_author_counts():
    cookbooks = [
        Cookbook('Pat Viafore'),
        Cookbook('Pat Viafore'),
        Cookbook('J K Rowling'),
    ]
    assert create_author_count_mapping(cookbooks) == {
        'Pat Viafore': 2,
        'J K Rowling': 1,
    }


test_author_counts()
