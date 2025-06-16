class Pizza:
    """
    Represents a single pizza with a crust, sauces, cheese, and toppings.

    The cost is calculated at initialization based on selected ingredients.
    """
    def __init__(self, crust, sauces, cheese, toppings):
        """
        Initialize a new Pizza instance. Calculates cost of pizza upon
        initialization.

        :param crust: The type of crust.
        :type crust: str
        :param sauces: A list of sauces applied to the pizza.
        :type sauces: list
        :param cheese: The cheese selection for the pizza.
        :type cheese: str
        :param toppings: A list of toppings added to the pizza.
        :type toppings: list
        """
        self.crust = crust
        self.sauces = sauces
        self.cheese = cheese
        self.toppings = toppings
        self.cost = self._cost()

    def __str__(self):
        """
        Return a string representation of the pizza, including ingredients and 
        cost.

        :return: A formatted string describing the pizza.
        :rtype: str
        """
        return f"Crust: {self.crust}, Sauce: {self.sauces}, Cheese: " \
            f"{self.cheese}, Toppings: {self.toppings}, Cost: {self.cost}"

    def _cost(self):
        """
        Internal method to calculate the total cost of the pizza. Costs are 
        based on the pizza's ingredients.

        :return: The total price of the pizza.
        :rtype: int
        """
        crust_costs = {"thin": 5,
                       "thick": 6,
                       "gluten_free": 8
                       }
        sauce_costs = {"marinara": 2,
                       "pesto": 3,
                       "liv_sauce": 5
                       }
        topping_costs = {"pineapple": 1,
                         "pepperoni": 2,
                         "mushroom": 3
                         }
        cost = 0
        cost += crust_costs[self.crust]
        cost += sum(sauce_costs[sauce] for sauce in self.sauces)
        cost += sum(topping_costs[topping] for topping in self.toppings)

        return int(cost)