# Create a directory to store name a places
place_visit = {}

#Laddar input frågan i en variabel att användas senare
prompt = "Vi skulle vilja höra vad ditt favoritresemål är"
prompt += '\nSå, vad är ditt namn? '

#sätter en Flagga
active_chk = True

while active_chk == True:
    name = input(prompt)
    place = input("\nVilket ställe skulle du vilja åkat till? ")

    #Lägger till namn och plats i directory
    place_visit[name] = place

    #Frågar om någon annan vill fortsätta fylla i
    quest = input("Vill någon annan skriva i sitt önskemål? (ja/nej) ")
    if quest == 'nej':
        active_chk = False

print("\n---- Här är sammanställningen ----")
#Skriver ut personers namn och önskemål om plats dom vill åka till!

for name, place in place_visit.items():
    print(f"{name.title()} vill åka till {place}")