#guest list creation
guests = ['nina','robin','linnéa']
print(f"I hereby invite you {guests[0].title()} to dinner on New Year's Eve!")
no_show = guests.pop(2)
print(f"Sorry you couldn't make it {no_show.title()} :-(")
print(guests)
guests.append('toffe')
print(guests)
guests.insert(0,'anna-clara')
guests.insert(2, 'kevve')
print(guests)
print("Sorry I can only invite two guests :-(")
guest_remove = guests.pop()
print(f"Sorry {guest_remove.title()} I can't have you at my party!")
guest_remove = guests.pop()
print(f"Sorry {guest_remove.title()} I can't have you at my party!")
guest_remove = guests.pop()
print(f"Sorry {guest_remove.title()} I can't have you at my party!")
print(f"I'm happy to still be able to invite you guys, {guests[0]} and {guests[1]}, you are very welcome")
del guests[0]
del guests[0]
print(guests)
