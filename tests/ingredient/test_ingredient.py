from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    arroz = Ingredient("arroz")
    feijao = Ingredient("feijao")
    manteiga = Ingredient("manteiga")
    assert manteiga.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
    }

    assert arroz.name == "arroz"
    assert feijao.name == "feijao"
    assert manteiga.name == "manteiga"

    assert hash(arroz) == hash("arroz")
    assert hash(feijao) == hash("feijao")
    assert hash(manteiga) == hash("manteiga")

    assert repr(arroz) == "Ingredient('arroz')"
    assert repr(feijao) == "Ingredient('feijao')"

    assert arroz != feijao
