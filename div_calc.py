print('Ge mig två nummer så ska jag dividera dom!!')
print("Skriv 'a' för att avsluta!!")

while True:
    first_num = input('Ge mig första numret!: ')
    if first_num == 'a':
        break
        
    sec_num = input('Ge mig andra numret!: ')
    if sec_num == 'a':
        break

    try:
        answer = int(first_num) / int(sec_num)

    except ZeroDivisionError:
        print('Du kan inte dividera med 0')
    else:
        print(answer)