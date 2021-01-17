check_for10 = input("Fyll i ett nummer så ska vi se om det är jämnt delbart med 10: ")

if not int(check_for10) % 10:
    print("Ditt nummer är en multipel av 10")
else:
    print("Ditt nummer är inte en multipel av 10")
