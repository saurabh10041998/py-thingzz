# Take a meal recipe, and change in number of servings
# and adjust each ingredients according to new servings.
# First element is a number and Rest elements is of
# form (ingredient, amount, unit) such as ("flour", 1.5, "cup")
def adjust_recipe(recipe, servings):
    new_recipe = [servings]
    old_servings = recipe[0]
    factor = servings / old_servings
    recipe.pop(0)
    while recipe:
        ingredient, amount, unit = recipe.pop(0)
        new_recipe.append((ingredient, amount * factor, unit))
    return new_recipe


def test_adjust_recipe():
    old_recipe = [2, ("flour", 1.5, "cups")]
    adjusted = adjust_recipe(old_recipe, 4)
    assert adjusted[1] == ("flour", 3, "cups")
    assert old_recipe == []

test_adjust_recipe()
