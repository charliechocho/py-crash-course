my_records_db = {}

for repeat in range(3):    
    art = input('Skriv in artist: ')
    my_records_db[art] = [] 
    alb = input('Skriv in album: ')
    yr = input('Skriv in år: ')

    my_records_db[art].append((alb,yr))


for key, value in my_records_db.items():
    print(f"Album jag har med {key}, och vilket år det är ifrån: \n")
    print(f"Album: {value[0][0]} som släpptes år: {value[0][1]} ")
        


