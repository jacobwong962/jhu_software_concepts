class Pizza:
#Pizza objects and associated cost
    def __init__(self, crust, sauces, cheese, toppings):
        self.crust = crust
        self.sauces = sauces
        self.cheese = cheese
        self.toppings = toppings
        self.cost = self._cost()
        #Initializes a pizza
        #Set pizza variables
        #Set cost to create

    def __str__(self):
        return f"Crust: {self.crust}, Sauce: {self.sauces}, Cheese: {self.cheese}, Toppings: {self.toppings}, Cost: {self.cost}"

    def _cost(self):
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

        return cost