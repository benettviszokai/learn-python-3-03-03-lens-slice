# Len's Slice

# Creating a list of toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Creating a list of prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Counting the 2s in the prices list
num_two_dollar_slices = prices.count(2)

# Toppings' length
num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Creating a two dimensional list from existing lists - prices with toppings
pizza_and_prices = [
  [prices[0], toppings[0]],
  [prices[1], toppings[1]],
  [prices[2], toppings[2]],
  [prices[3], toppings[3]],
  [prices[4], toppings[4]],
  [prices[5], toppings[5]],
  [prices[6], toppings[6]],
]

# Sorting and Slicing Pizzas

# Sorting the list (ascending - increasing price)
pizza_and_prices.sort(); # This method sorts the original list without return value

# First element from the list
cheapest_pizza = pizza_and_prices[0]

# Last element from the list
priciest_pizza = pizza_and_prices[-1]

# Removing the last element from the list
pizza_and_prices.pop() # Pop used this way removes the last element from the list but also capable to remove an element with a specified index

# Adding an element to the list with index
pizza_and_prices.insert(4, [2.5, "Peppers"])

# The first 3 element from the list
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
