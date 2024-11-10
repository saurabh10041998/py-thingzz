from typing import TypedDict
from pprint import pprint


class Range(TypedDict):
    min: float
    max: float


class NutritionInformation(TypedDict):
    value: int
    unit: str
    confidenceRange95Percent: Range
    standardDeviation: float


class RecipeNutritionInformation(TypedDict):
    recipe_used: int
    calorie: NutritionInformation
    fat: NutritionInformation
    protein: NutritionInformation
    carbs: NutritionInformation


recipe_name = 'Vada Pav'
def get_recipe_nutrition_information(recipe: str):
    return RecipeNutritionInformation({
        'recipe_used': 1,
        "calorie": {
            'value': 1,
            'unit': 'g',
            'confidenceRange95Percent': {
                'min': 1,
                'max': 2
            },
            'standardDeviation': 3.5
        },
        "fat": {
            'value': 1,
            'unit': 'g',
            'confidenceRange95Percent': {
                'min': 1,
                'max': 2
            },
            'standardDeviation': 3.5
        },
        "protein": {
            'value': 1,
            'unit': 'g',
            'confidenceRange95Percent': {
                'min': 1,
                'max': 2
            },
            'standardDeviation': 3.5
        },
        "carbs": {
            'value': 1,
            'unit': 'g',
            'confidenceRange95Percent': {
                'min': 1,
                'max': 2
            },
            'standardDeviation': 3.5
        }

    })


recipe_info: RecipeNutritionInformation = get_recipe_nutrition_information(recipe_name)

pprint(recipe_info)
