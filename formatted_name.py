def grup_db_add(artist_group):
    grp_art = input('Skriv in gruppen du vill lägga till i din databas: > ')
    if grp_art == 'q':
        print("See you around!!")
        break 
    else:
        my_records[grp_art] = []
        group_db_add(grp_art)


def album_db_add(group_album):
    """Organize Group/ARtist and add to DB"""
    while True:
        albm = input('Skriv in album ett album med en här artisten: > ')
    
        if albm == 'q':
            break
        else:
            if group_album == '':
                print("Du har inte fyllt i någon artist!!")
                break            
            else:
                my_records[group_album].append(albm)
         

def print_catalogue(record_db):
    for key, value in my_records.items():
        for album in value:
            print(f"{album.title()} album by {key.title()}")



my_records = {}


while true:
    grp_receive = group_db_add(grp_art)
    full_grp_cat = album_db_add(grp_receive)


print_catalogue(my_records)

