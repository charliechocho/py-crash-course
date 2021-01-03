#sort a list permanently with .sort() method
cars = ['bmw','saab','audi','volvo','tesla']
#cars.sort()

for car in cars:
    if len(car.lower()) < 5:
        print(car.upper())
    else:
        print(car.title())

print('subaru' not in cars)

print(f"\nThere are {len(cars)} cars in the garage")

print(cars[2] == 'audi')
print(len(cars) > 6)
print('volvo' in cars or 'ferrari' in cars)
print('volvo' in cars and 'ferrari' in cars)
cars.append('ferrari')
print('volvo' in cars and 'ferrari' in cars)
car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False")
print(car == 'audi')
print(len(cars) <= 6)
