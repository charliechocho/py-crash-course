age = 3
admission_fee = (0,25,40)

if age < 4:
    print(f"Your admission fee is ${admission_fee[0]}, welcome to the park!")
elif age < 18:
    print(f"Your admission fee is ${admission_fee[1]}, welcome to the park!")
else:
    print(f"You're a senior so your fee is ${admission_fee[2]}, Welcome!!")
