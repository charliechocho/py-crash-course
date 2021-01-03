alien_0 = {'color':'green', 'speed':'slow'}

point_value = alien_0.get('points')

if point_value == None:
    alien_0['points'] = '5'
    print("Adding 'points' to dictionary!\n")
    print(alien_0['points'])
else:
    print(point_value)


