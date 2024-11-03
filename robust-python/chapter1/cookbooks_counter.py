from collections import Counter
from dataclasses import dataclass
from typing import List
from typing import Mapping

@dataclass
class Cookbook:
    author: str


def create_author_count_mapping(
    cookbooks: List[Cookbook]
) -> Mapping[str, int]:
    return Counter(cookbook.author for cookbook in cookbooks)


def test_author_create_count():
    cookbooks = [
        Cookbook('Pat Viafore'),
        Cookbook('Pat Viafore'),
        Cookbook('J K Rowling'),
    ]
    assert create_author_count_mapping(cookbooks) == {
        'Pat Viafore': 2,
        'J K Rowling': 1,
    }


test_author_create_count()
