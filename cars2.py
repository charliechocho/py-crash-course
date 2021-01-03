#sort a list permanently with .sort() method
cars = ['bmw','saab','audi','volvo','tesla']
cars.sort(reverse = True)
print(cars)

#Sort temporarily with the sorted() function
print("Here is the original list:")
cars = ['bmw','saab','audi','volvo','tesla']
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars, reverse = True))
print("\nAnd here is the original list again")
print(cars)

#reverse the order of a list
print(f"\n{cars}")
cars.reverse()
print(f"\n{cars}")