from dataclasses import dataclass
from typing import List
from typing import Dict


@dataclass
class Cookbook:
    author: str

def create_author_count_mapping(
    cookbooks: List[Cookbook]
) -> Dict[str, int]:
    counter = {}
    for cookbook in cookbooks:
        if cookbook.author not in counter:
            counter[cookbook.author] = 0
        counter[cookbook.author] += 1
    return counter


def test_authors_count():
    cookbooks = [
        Cookbook('Pat Viafore'),
        Cookbook('Pat Viafore'),
        Cookbook('J K Rowling'),
    ]
    assert create_author_count_mapping(cookbooks) == {
        'Pat Viafore': 2,
        'J K Rowling': 1,
    }


test_authors_count()
