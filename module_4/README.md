# Name: Jacob Wong (jwong86)

# Module 4 Assignment 
## Pytest and Sphinx due on 06/17/2025 at 11:59 EST

# My Pizza Ordering Application:
ReadtheDocs Link:
https://module-4-pizza-application.readthedocs.io/en/latest/order.html

# Approach:
My Pizza Ordering application was built with two modules:
- order.py
- pizza.py
These modules were built with fairly simple code, utilizing Classes to represent Pizza objects, and Order objects. The Pizza objects were built with very simple functionality, with the ability to define all of the pizza's toppings and the pizzas' corresponding price. The Order class consisted of a method to add pizzas to an order and to flag whether a pizza has been ordered or not.

This application was developped using Test-Driven Development. Each method in the classes had a corresponding unit test, and the to modules were tested together in a single integration test. These tests were carried out using the pytest framework. Each test was denoted with a marker indicating it being an 'order' test or a 'pizza' test. The pizza test module also used a fixture to instantiate a pizza object. All tests have been confirmed to pass.

Both modules were documented using Sphinx docstrings. We generated html for the documentation in the ReadtheDocs format. The documentation is presented online with the link shared above.

# Known Bugs:
None