infinte_loop = input("Skriv startnummer så ska jag skriva ut alla jämna nummer: ")

num = int(infinte_loop)

while num < 2_000_000:
    if num % 2 == 0:
        print(num)
        num += 1 
    else:
        num += 1


