number_ordinals = list(range(1,10))
print(number_ordinals)

for num in number_ordinals:
    if num < 2:
        print(f"{num}st")
    elif num < 3:
        print(f"{num}nd")
    elif num < 4:
        print(f"{num}rd")
    else:
        print(f"{num}th")
