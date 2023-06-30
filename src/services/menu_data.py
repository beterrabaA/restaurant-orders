import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, 'r') as file:
            readed_file = csv.DictReader(file)
            menu = list(readed_file)
        dishes = {}

        for item in menu:
            receita = item["dish"]
            preco = float(item["price"])
            ingredientes = Ingredient(item['ingredient'])
            quantidade = float(item["recipe_amount"])
            if receita not in dishes:
                dishes[receita] = Dish(receita, preco)
            dishes[receita].add_ingredient_dependency(ingredientes, quantidade)
        self.dishes = set(dishes.values())

