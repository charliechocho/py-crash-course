my_records = ['beatles','abba','elp','toni braxton','jethro tull','celine dion','jennie abrahamsson']
collection_size = len(my_records)
print(f"I have {collection_size} records in my collection and they are: \n{my_records}")

#temp sort them
print(f"Here they are in a sorted order so you can follow better, \n{sorted(my_records)}")

#reversing the order of the list
my_records.reverse()
print(f"here is the list in reverse non alphabetical order: \n{my_records})")

#store new list for saving to file

my_records.sort()
print(f"Here is a sorted list for storing in DB file: \n{my_records}")

#sort permanently backwards
my_records.sort(reverse=True)
print(f"Here you have my record collection in a backwards order: \n{my_records}")

print(f"My favorite record is: \n\n{my_records[3].upper()}")

my_records.insert(0, 'journey')
my_records.insert(0, 'gazebo')
my_records.insert(0, 'lime')

print(f"I just bought some new records! I used to have {collection_size} records but now I have {len(my_records)}")
print(f"here they are in alphabetical order: \n{sorted(my_records)}")

sold_record = my_records.pop(2)
print(f"Ooooops sold one, because I didn't like {sold_record}")
print(my_records)
my_records.sort()
print(my_records)
