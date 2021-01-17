add_on = "\nLägg till en topping: "
add_on += "\nSkriv 'quit' när du är klar: "

topping = ""

while topping.lower() != 'quit':
    topping = input(add_on)
    if topping.lower() != 'quit':
        print(f"Lägger till {topping.title()} till din beställning!")
