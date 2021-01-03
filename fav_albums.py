fav_albums = {
    'elp':'karnevil 9',
    'ayreon':'final experiment',
    'marillion':'misplaced childhood',
    'magnum':"on a storteller's night",
}
print("These are my all time favorite albums!!")
for key, value in fav_albums.items():
    print(f"\n\t{value.title()} by {key.upper()}!")

print("My favorite artists:")
order = 0

for artist in fav_albums.keys():
    order += 1
    print(f"My number #{order} artist is {artist}")

order = 0

for album in fav_albums.values():
    order += 1
    print(f"\tMy number #{order} album is {album}")

for artist in sorted(fav_albums.values()):
    print(artist)