# Printa variabeln name och name_2 med olika stripping och formatering
name = "Nina"
print(f"Hello, {name}! Would you like to learn some python?")
name_2 = "nina pentti"
print(name_2)
print(name_2.upper())
print(name_2.title())
quote = '"A person who never made a mistake, never tried anything new"'
fam_person = " Albert Einstein "
print(f"A wise person once said, {quote}\n\t-{fam_person.strip()}!")