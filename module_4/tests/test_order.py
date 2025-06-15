import pytest
from src.order import Order
from src.pizza import Pizza

@pytest.fixture
def example_pizza():
    return Pizza("thin", ["pesto"], "mozzarella", ["mushroom"])


@pytest.mark.order
def test_init():
    order = Order()
    assert order.pizzas == []
    assert order.cost == 0
    assert order.paid is False
    
@pytest.mark.order
def test_str(example_pizza):
    order = Order()
    order.input_pizza(example_pizza)
    expected_output = (
        "Customer Requested:\n"
        "Crust: thin, Sauce: ['pesto'], Cheese: mozzarella, Toppings: ['mushroom'], Cost: 11"
    )
    assert str(order) == expected_output

@pytest.mark.order
def test_input_pizza(example_pizza):
    order = Order()
    order.input_pizza(example_pizza)
    assert example_pizza in order.pizzas
    assert order.cost == example_pizza.cost()

@pytest.mark.order
def test_order_paid():
    order = Order()
    assert order.paid is False
    order.order_paid()
    assert order.paid is True