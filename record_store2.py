vinyl_0 = {
    'artist':'abba',
    'album':'visitors',
    'year':'1981',
    'genre':'pop',
    'form': ['cd','vinyl','casette'],
}
vinyl_1 = {
    'artist':'abba',
    'album':'super trouper',
    'year':'1980',
    'genre':'pop',
    'form': ['na','vinyl','casette'],
}
vinyl_2 = {
    'artist':'abba',
    'album':'voulez vous',
    'year':'1979',
    'genre':'pop',
    'form': ['cd','vinyl','na'],
}

record_store = [vinyl_0, vinyl_1, vinyl_2]

print(f"I have {len(record_store)} albums of Abba:\n")

for record in record_store:
    print(f"\tFrom {record['year']} I have {record['album'].title()}")

    for forms in record['form']:
        if forms != 'na':
            print(f"\n\t\tAvailable as: {forms}")
    

