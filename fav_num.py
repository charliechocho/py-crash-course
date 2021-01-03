fav_num = {
    'nina':'7',
    'mattias':'9',
    'andreas':'13',
    'daniel':'12',
    'anna-clara':'12',
}

for key, value in fav_num.items():
    if not key[-1] == 's':
        print(f"{key.title()}'s favorite number is {value}")
    else:
        print(f"{key.title()}' favorite number is {value}")


for value in sorted(set(fav_num.values()), reverse = True):
    print(value)