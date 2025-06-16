import pytest
from src.pizza import Pizza

@pytest.fixture
def example_pizza():
    """Test fixture that instantiates a Pizza object."""
    return Pizza("thin", ["pesto"], "mozzarella", ["mushroom"])

@pytest.mark.pizza
def test_init(example_pizza):
    """
    Unit test for the Pizza class constructor. Verifies that all instance
    variables are created and that the cost of the pizza is non-zero.
    """
    assert isinstance(example_pizza, Pizza)
    assert example_pizza.crust == "thin"
    assert example_pizza.sauces == ["pesto"]
    assert example_pizza.cheese == "mozzarella"
    assert example_pizza.toppings == ["mushroom"]
    assert example_pizza.cost > 0
    
@pytest.mark.pizza
def test_str(example_pizza):
    """
    Unit test that verifies that __str__() returns a string in the proper 
    format.
    """
    assert str(example_pizza) == (
        "Crust: thin, Sauce: ['pesto'], Cheese: " 
        "mozzarella, Toppings: ['mushroom'], Cost: 11"
        )

@pytest.mark.pizza
def test_cost(example_pizza):
    """
    Unit test that verifies that _cost() correctly calculates the total cost of
    the pizza.
    """
    assert example_pizza._cost() == 11