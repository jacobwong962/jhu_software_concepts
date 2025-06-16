from pizza import Pizza
class Order:
    def __init__(self):
        self.pizzas = []
        self.cost = 0
        self.paid = False

    def __str__(self):
        str_response = f"Customer Requested:\n"
        for pizza in self.pizzas:
            str_response += str(pizza)
            str_response += "\n"
        return str_response

    def input_pizza(self, crust, sauce, cheese, toppings):
        #Input the customers order for a given pizza
        #Initialize the pizza object and attach to the order
        #Update the cost
        pizza = Pizza(crust, sauce, cheese, toppings)
        self.pizzas.append(pizza)
        self.cost += pizza.cost

    def order_paid(self):
        #Set order as paid once payment has been collected
        self.paid = True

if __name__ == "__main__":
    order = Order()
    order.input_pizza("thin", ["pesto"], "mozzarella", ["mushroom"])
    order.input_pizza("thick", ["marinara"], "mozzarella", ["mushroom"])
    print(order)