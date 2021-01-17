current_number = 0

#continue in a loop ignores value and loops without doing anyging
while current_number < 10:
    current_number += 1
    if current_number % 3 != 0:
        continue

    print(current_number)