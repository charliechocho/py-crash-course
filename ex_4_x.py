#list comprehension makes code even shorter but harder to read
num_square = [value**3 for value in range(1,10)]

#showing the long way of doing this
num_square = []

for value in range(3,31,3):
	num_square.append(value)

print(num_square)

#the medium way of doing it
num_square = []

for value in range(1,11):
	num_square.append(value**3)

print(num_square)
print(min(num_square))
print(max(num_square))
print(sum(num_square))
