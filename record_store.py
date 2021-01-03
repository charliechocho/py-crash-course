vinyls = {'artist':'abba', 'album':'visitors', 'year':'1980'}

for key, value in vinyls.items():
    print(f"{key}:{value}")

vinyls['album'] = 'Super Trouper'

print(vinyls)

vinyls['genre'] = 'pop'

print(vinyls)

if vinyls['year'] == '1981':
    vinyls['album'] = 'visitors'
elif vinyls['year'] == '1980':
    vinyls['album'] = 'super trouper'
elif vinyls['year'] == '1979':
    vinyls['album'] = 'voulez vous'

del vinyls['genre']
print(vinyls)