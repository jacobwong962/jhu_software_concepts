import pytest
from src.pizza import Pizza

@pytest.fixture
def example_pizza():
    return Pizza("thin", ["pesto"], "mozzarella", ["mushroom"])

@pytest.mark.pizza
def test_init():
    assert
    