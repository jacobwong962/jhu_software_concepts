import pytest
from src.pizza import Pizza

@pytest.fixture
def example_pizza():
    return Pizza("thin", ["pesto"], "mozzarella", ["mushroom"])

@pytest.mark.pizza
def test_init(example_pizza):
    assert isinstance(example_pizza, Pizza)
    assert example_pizza.crust == "thin"
    assert example_pizza.sauces == ["pesto"]
    assert example_pizza.cheese == "mozzarella"
    assert example_pizza.toppings == ["mushroom"]
    assert example_pizza.cost > 0
    
@pytest.mark.pizza
def test_str(example_pizza):
    assert str(example_pizza) == "Crust: thin, Sauce: ['pesto'], Cheese: mozzarella, Toppings: ['mushroom'], Cost: 11"

@pytest.mark.pizza
def test_cost(example_pizza):
    assert example_pizza.cost() == 11