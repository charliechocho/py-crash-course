players = ['mattias','andreas','robin','daniel','linnéa']

#find the middle
the_odd_one = len(players)%2
print(the_odd_one)
middle = len(players)/2
print(int(middle))
print(f"The middle name of the list is {players[int(middle)]} ")
print(f"The last names from the middle are:\n {players[int(middle):]} ")

middle_end = [print(name) for name in players[int(middle):]]
