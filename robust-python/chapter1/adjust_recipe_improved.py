import copy

from dataclasses import dataclass
from fractions import Fraction
from typing import List

@dataclass
class Ingredient:
    name: str
    amount: Fraction
    units: str


    def adjust_proportion(self, factor: Fraction):
        self.amount *= factor

@dataclass
class Recipe:
    servings: int
    ingredients: List[Ingredient]

    def clear_ingredients(self):
        self.ingredients.clear()

    def get_ingredients(self):
        return self.ingredients


# Take a meal and adjust number of servings
# Recipe is class representing a recipe
def adjust_recipe(old_recipe: Recipe, servings: int) -> Recipe:
    # make a copy of ingredients of old_recipe
    new_ingredients = list(old_recipe.get_ingredients())
    old_recipe.clear_ingredients()
    for ingredient in new_ingredients:
        ingredient.adjust_proportion(Fraction(servings, old_recipe.servings))
    return Recipe(servings, new_ingredients)


def test_adjust_recipe():
    old_recipe = Recipe(2, [Ingredient('flour', 1.5, 'cups')])
    adjusted = adjust_recipe(old_recipe, 4)
    assert Recipe(4, [Ingredient('flour', 3, 'cups')]) == adjusted
    assert old_recipe.ingredients == []


test_adjust_recipe()
