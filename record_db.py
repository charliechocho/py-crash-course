def group_db_add():
    """Get the name of the Group/Artist"""
    grp_art = input('Skriv in gruppen du vill lägga till i din databas: > ')
    if grp_art == 'q':
        print("See you around!!")
        return 'q'
    elif grp_art.lower() in my_records:
        print(f"\n\tGruppen/Artisten {grp_art} finns redan! Lägga till en annan!")
        return 'duplicate'
    else:
        my_records[grp_art.lower()] = []
        return grp_art.lower()


def album_db_add(group_album):
    """Organize Group/ARtist and add to DB"""
    #get the artist and add albums throug input
    while True:
        prompt = "Skriv in album ett album med en här artisten:"
        prompt += "(Skriv 'q' för att avbryta inmatning > "
        albm = input(prompt)
        year = input("Vilket år: > ")
    
        if albm == 'q':
            break
        else:
            if group_album == '':
                print("Du har inte fyllt i någon artist!!")
                break            
            else:
                my_records[group_album].append((albm, year))
         

def print_catalogue(record_db):
    """Prints the albums and artists and the year"""
    for key, value in my_records.items():
        print(f"\nAdded these albums by {key.title()}")
        for album in sorted(value):
            print(f"\t{album[0].title()} som släpptes år: {album[1]}")


def add_db():
    """Starts up the DB and prepares for adding new items"""    
    active = True

    while active:
        grp_receive = group_db_add()
        if grp_receive == 'duplicate':
            continue
        elif grp_receive != 'q':
            full_grp_cat = album_db_add(grp_receive)
        else:
            active = False

def create_db():
    """Creates the Data base initial Dictionary that will hold keys and values"""
    db_name = {}
    return db_name

my_records = create_db()
add_db()
print_catalogue(my_records)

