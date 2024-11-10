from collections import defaultdict
from typing import Generic
from typing import NewType
from typing import TypeVar
from typing import Dict
from typing import List

Restaurant = NewType('Restaurant', str)
Recipe = NewType('Recipe', str)

Node = TypeVar('Node')
Edge = TypeVar('Edge')

class Graph(Generic[Node, Edge]):
    def __init__(self):
        self.edges:Dict[Node, List[Edge]] = defaultdict(list)

    def add_relation(self, node: Node, to: Edge):
        self.edges[node].append(to)

    def get_relations(self, node:Node) -> List[Edge]:
        return self.edges[node]

restaurants: Graph[Restaurant, Restaurant] = Graph()
recipes: Graph[Recipe, Recipe] = Graph()

restaurants_recipes: Graph[Restaurant, Recipe] = Graph()

recipes.add_relation(Recipe('Vada Pav'), Recipe('Chai'))

restaurants.add_relation(Restaurant('Laxmi Vada Pav'),
                         Restaurant('Shinde tea stall'))

# invalid case
#recipes.add_relation(Restaurant('Laxmi Vada Pav'),
#                     Restaurant('Shinde tea stall'))


