question = "\nBiljett pris beror på ålder!"
question += "\nSå, hur gammal är du? "

age = ""

while True:
    age = input(question)

    if int(age) <= 0:
        print("\nHejdå Välkommen Åter!")
        break
    elif int(age) < 3:
        print(f"Du går in gratis")
    elif int(age) < 12:
        print("Ditt pris är 90.- då du är under 12 år")
    else:
        print("Då du är över 12 år är ditt pris 130.-")