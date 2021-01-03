my_pizzas = ['caprisiosa','vesuvio','ciao ciao','margerita','diavolo']

friends_pizza = my_pizzas[:]

print(my_pizzas)
print(friends_pizza)

my_pizzas.append('kaiser söse')
friends_pizza.append('napolitana')

print(f"My favorite pizzas are:\n {my_pizzas}")
print(f" My friends favorites are:\n {friends_pizza}")

for pizza in my_pizzas:
	print(pizza)

for friendpizza in friends_pizza:
	print(friendpizza)