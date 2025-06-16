from pizza import Pizza
class Order:
    """
    Represents a customer's pizza order, which can include multiple pizzas.

    Tracks the list of pizzas, total cost, and payment status.
    """
    def __init__(self):
        """
        Instantiates an Order class object. 
        """
        self.pizzas = []
        self.cost = 0
        self.paid = False

    def __str__(self):
        """
        Return a string representation of the order.

        :return: Description of all pizzas in the order.
        :rtype: str
        """
        str_response = f"Customer Requested:\n"
        for pizza in self.pizzas:
            str_response += str(pizza)
            str_response += "\n"
        return str_response

    def input_pizza(self, crust, sauce, cheese, toppings):
        """
        Add a new pizza to the order and update the total cost.

        :param crust: The type of crust (e.g., "thin", "gluten_free").
        :type crust: str
        :param sauce: A list of sauces to apply.
        :type sauce: list
        :param cheese: The cheese selection.
        :type cheese: str
        :param toppings: A list of toppings to add.
        :type toppings: list
        """
        pizza = Pizza(crust, sauce, cheese, toppings)
        self.pizzas.append(pizza)
        self.cost += pizza.cost

    def order_paid(self):
        """
        Mark the order as paid by setting the `paid` attribute to True.
        """
        self.paid = True

if __name__ == "__main__":
    order = Order()
    order.input_pizza("thin", ["pesto"], "mozzarella", ["mushroom"])
    order.input_pizza("thick", ["marinara"], "mozzarella", ["mushroom"])
    print(order)