prompt = "\nEnter cities you've visited"
prompt += "\nEnter quit when you're finished! "
cities = []


while True:
    place = input(prompt)
    if place == 'quit':
        break
    else:
        print(f"I've always wanted to go to {place.title()}!!")
        cities.append(prompt)

for city in cities:
    print(city.title())