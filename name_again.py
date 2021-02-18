from name_function import format_name

print("Skriv 'a' för att avsluta inmatning")

while True:
    first = input("\nVad är ditt förnamn? ")
    if first == 'a':
        break

    last = input("\nVad är ditt efternamn? ")
    if last == 'a':
        break
    full_name = format_name(first, last)
    print(f"\n\tSå ditt fulla namn är: {full_name}.")