sandwiches = ['roast beef', 'chicken', 'blt', 'bologna', 'roast beef', 
'cheese & ham', 'shrimp', 'roast beef']

finished_sandwiches = []
order = 1

while sandwiches:
    make_sandwich = sandwiches.pop()

    print(f"\nNow preparing order #{order} a {make_sandwich.title()} sandwich!")
    finished_sandwiches.append(make_sandwich)
    order += 1

print("\n--- Sandwiches ready for pickup!! ---")

for sandwich in finished_sandwiches:
    print(f"Your {sandwich.title()} sandwich is ready!!")

print("\n\nSorry, We're now all out of Roast Beef! Here is the New Menu")

while 'roast beef' in finished_sandwiches:
    finished_sandwiches.remove('roast beef')

menu_item = 1

for sandwich in finished_sandwiches:
    print(f"{menu_item}. {sandwich.title()} Sandwich")
    menu_item += 1
