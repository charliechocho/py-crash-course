file_name = 'guest_book.db'
file_path = '/Users/towertwenty/db_files/'


def name_input():
    name  = input("What's your first name? ('q')\t")
    if name == 'q':
        return 'no_more'
    else:
        last_name = input("What's your last name?\t")
        full_name = f"{name.title()} {last_name.title()}"
        return full_name

active = True   

with open(f'{file_path}{file_name}', 'a') as file_obj:
    while active == True:
        db_entry = name_input()
        if db_entry == 'no_more':
            active = False
        else:
            print(f"Hej och välkommen {db_entry}!!")
            file_obj.write(
        f"""Välkommen till oss {db_entry}!! Trevligt att ha dig hos oss!\n""")

print('Tack och välkommen åter!!')


