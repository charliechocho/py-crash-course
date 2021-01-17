persons = input("Hur många blir ni i ert sällskap?")

if int(persons) > 8:
    print("Jag är ledsen men vi kan ta emot max 8 personer")
else:
    print(f"Då gör jag en reservation för {persons} peroner! Välkomna!")