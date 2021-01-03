multi_aliens = []

for alien in range(30):
    new_alien = {'color':'green','points':'5','speed':'slow'}
    multi_aliens.append(new_alien)

for alien in multi_aliens:
    print(alien)

print(f"\n{len(multi_aliens)} aliens created")


for alien in multi_aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'

for alien in multi_aliens[:10]:
    print(alien)