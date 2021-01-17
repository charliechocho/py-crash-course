cars_in_stock = ['volvo','saab','volkswagen','bmw','toyota','mercedes']
car = input("What kind of car would you like? (enter a brand): ")

if car.lower() in cars_in_stock:
    print(f"We actually hava a {car.title()} that you can have! ")
else:
    print(f"Unfortunately we don't have that brand! We have these!")
    no = 0
    for brand in cars_in_stock:
        print(f"\t{no}. {brand.title()}")
        no += 1

    no = input("Which one do you want? Enter number: ")
    selected_car = cars_in_stock[int(no)]

    print(f"Getting you a {selected_car.title()}! Enjoy your ride!")

