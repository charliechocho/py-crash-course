def my_pet(pet_type = 'alien', pet_name = 'ET'):
    """display pet and its name"""
    print(f"I have a {pet_type.title()}!")
    print(f"\tMy {pet_type.title()}'s name is {pet_name.title()}\n")

pet_type = input("Vad har du för husdjur? ")
pet_name = input("Vad heter ditt djur? ")
my_pet(pet_type, pet_name)

