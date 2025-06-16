import pytest
from src.order import Order
from src.pizza import Pizza

@pytest.mark.order
def test_init():
    """
    Unit test to verify that constructor initializes all of the instance
    variables.
    """
    order = Order()
    assert order.pizzas == []
    assert order.cost == 0
    assert order.paid is False
    
@pytest.mark.order
def test_str():
    """Unit test to verify that the __str__ method is properly formatted."""
    order = Order()
    order.input_pizza("thin", ["pesto"], "mozzarella", ["mushroom"])
    expected_output = (
        "Customer Requested:\n"
        "Crust: thin, Sauce: ['pesto'], Cheese: mozzarella, Toppings: "
        "['mushroom'], Cost: 11\n"
    )
    assert str(order) == expected_output

@pytest.mark.order
def test_input_pizza():
    """
    Unit test to verify that input_pizza() correctly calculates the cost of
    the pizza.
    """
    order = Order()
    order.input_pizza("thin", ["pesto"], "mozzarella", ["mushroom"])
    assert order.cost == 11

@pytest.mark.order
def test_order_paid():
    """
    Unit test to verify that order_paid() successfully sets 'paid' attribute to
    True.
    """
    order = Order()
    assert order.paid is False
    order.order_paid()
    assert order.paid is True