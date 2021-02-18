check = True
def add_num(num1, num2):
    try:
        solution = int(num1) + int(num2)

    except ValueError:
        print("Är du säker på att du angav två NUMMER?")
        return False


    else:
        print(f"Summan av dessa nummer blir {solution}")


while check != False:
    first_num = input('Enter first number: ')
    sec_num = input('Enter second number: ')
    check = add_num(first_num, sec_num)
