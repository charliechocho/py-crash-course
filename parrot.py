intro = "Hej och välkommen till denna enkät! Vi börjar med att lära känna \
dig lite granna! Skriv 'quit' om du vill sluta!"
intro += "\n\tVi börjar med vad du heter? "

storage = []

print(intro)
active = True

while active:
    message = input("Fyll i ditt förnamn: ")
    message_2 = input("Fyll i ditt efternamn: ")
    age = input("How Old are you?: ")

    if message and message_2:
        print(f"\nHej på dig {message.title()} {message_2.title()}\n")
        if int(age) > 65:
            print("\nOj en pensionär på min ära!! Njut av 52 veckor semester!!")
            storage.append(f"{message} {message_2}: {age}")
        else:
            print(f"\nDu har  {65 - int(age)} år kvar till 52 veckors semester!!")
            storage.append(f"{message} {message_2}: {age}")
    elif message == 'quit':
        active = False
        print("Ha en trevlig dag och välkommen åter!")
    else:
        print("Oj det verkar som du inte skrev i för- OCH efternamn. Försök igen")

for inserts in storage:
    print(inserts)