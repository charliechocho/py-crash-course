num_square = []
#the loong way to filling a list and calculate sqrt
for value in range(1,11):
	square = value ** 2
	num_square.append(square)

#a shorter way of doing it by calculating and appending in one go
for value in range(1,11):
	num_square.append(value**2)

print(num_square)

count = len(num_square)

for i in range(0,count):
	num_square[i] = num_square[i]//2

print(num_square)

#list comprehension makes the code even shorter, now we create list, calculate and loop append 
#in one go
num_square = [value**2 for value in range(1,11)]
print(f"\n{num_square}")

