file_path = '/Users/towertwenty/db_files/'
file_name = 'pi_million_digits.txt'

with open(f'{file_path}{file_name}') as file_object:
    lines = file_object.readlines()
    
pi_string = ''

for line in lines:
    pi_string += line.strip()

prompt = "Nu ska vi se om din födelsedag finns med i Pi's miljon första decimaler"
prompt += "\nSkriv in ditt födelsedatum enligt format (ååmmdd): "

print(prompt)
birthday = input("\n: ")

if birthday in pi_string:
    print("Din födelsedag finns med i Pi's första miljon av decimaler!!")
else:
    print("Din födelsedag finns inte med i Pi's första miljon av decimaler!!")

