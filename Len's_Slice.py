"""
You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data

quest1
To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:

    pepperoni
    pineapple
    cheese
    sausage
    olives
    anchovies
    mushrooms


quest2
To keep track of how much each kind of pizza slice costs, create a list called prices that holds:

    2
    6
    1
    3
    2
    7
    2


quest3
Find the length of the toppings list and store it in a variable called num_pizzas.

quest4
Print the string "We sell X different kinds of pizza!", with num_pizzas where the X is.

quest5
Use zip to combine the two lists into a list called pizzas that has the structure:

[(price_0, topping_0), (price_1, topping_1), (price_2, topping_2), ...]

In order to make the result of zip a list, do the following:

list(zip(____, ____))

quest6
Print pizzas.

Does it look the way you expect?

quest7
Sort pizzas so that the pizzas with the lowest prices are at the start of the list.

quest8
Store the first element of pizzas in a variable called cheapest_pizza.

quest9
A man in a business suit walks in and shouts “I will have your MOST EXPENSIVE pizza!”

Get the last item of the pizzas list and store it in a variable called priciest_pizza.

quest10
Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.

Slice the pizzas list and store the 3 lowest cost pizzas in a list called three_cheapest.

quest11
Print the three_cheapest list.

quest12
Your boss wants you to do some research on $2 slices.

Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out.


"""


#quest1
toppings=['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']
#quest2
prices=[2,6,1,3,2,7,2]
#quest3
num_pizzas=len(toppings)
#quest4
print("We sell ",num_pizzas," different kinds of pizza!")
#quest5
pizzas=list(zip(prices,toppings))
#quest6
print(pizzas)
#quest7
pizzas.sort()
#quest8
cheapest_pizza=pizzas[0]
#quest9
priciest_pizza=pizzas[-1]
#quest10
three_cheapest=pizzas[0:3]
#quest11
print(three_cheapest)
#quest12
num_two_dollar_slices=prices.count(2)
print(num_two_dollar_slices)
