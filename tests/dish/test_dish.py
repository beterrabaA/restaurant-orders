from src.models.ingredient import Ingredient, Restriction
from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    prato_1 = Dish("Pizza", 23.99)
    prato_2 = Dish("Carne de Sol", 45.99)

    assert prato_1.name == "Pizza"
    assert prato_2.name == "Carne de Sol"

    prato_1.add_ingredient_dependency(Ingredient("queijo parmesão"), 126)

    assert prato_1.get_restrictions() == {
        Restriction.LACTOSE,
          Restriction.ANIMAL_DERIVED
          }

    assert prato_1.get_ingredients() == {Ingredient("queijo parmesão")}

    assert repr(prato_1) == "Dish('Pizza', R$23.99)"
    assert repr(prato_2) == "Dish('Carne de Sol', R$45.99)"

    assert prato_1 == Dish("Pizza", 23.99)
    assert prato_2 == Dish("Carne de Sol", 45.99)

    assert prato_1 != prato_2

    assert hash(prato_1) == hash("Dish('Pizza', R$23.99)")
    assert hash(prato_2) == hash("Dish('Carne de Sol', R$45.99)")   

    with pytest.raises(TypeError):
        Dish("Pizza", "23.99")

    with pytest.raises(ValueError):
        Dish("Pizza", -23.99)