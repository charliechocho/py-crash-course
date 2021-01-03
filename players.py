players = ['mattias','andreas','robin','daniel','linnéa']
#players.sort(reverse=True)
print(players[-3:])


numbers = [value for value in range(1,10,2)]
print(numbers)

print("These are my first three players")

for name in players[:3]:
	print(name)

playorder = sorted(players[2:])
playorder.append('groover')
print(playorder)
print(players)	
