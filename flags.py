active = True

while active:
    message = input("Skriv något!! (enter 'q' to quit!): ")

    if message == 'q':
        active = False
    else:
        print(message)