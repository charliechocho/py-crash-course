filename = 'a_daughter_of_witches.txt'
file_path = 'txt_files/'

try:
    with open(f"{file_path}{filename}", encoding = 'utf-8') as f:
        contents = f.read()
        word_hunt = contents.lower().count('the ')
        print(f"Ordet du letar efter hittas {word_hunt} gånger i denna story")

except FileNotFoundError:
    print("Kan inte hitta boken du vill analysera!")

