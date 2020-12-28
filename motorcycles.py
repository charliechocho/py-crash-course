#crate lists with motorcycle brands to learn how to create, change and append
#create a list
motorcycles = ['honda','kawasaki','ducati','yamaha','suzuki','norton']
motorcycles_orig = motorcycles
print(motorcycles)
#change an item
motorcycles[5] = 'harley davidson'
print(motorcycles)
#add an item
motorcycles.append('norton')
print(motorcycles)
#build a list from scratch
motorcycles = []
motorcycles.append('bmw')
motorcycles.append('husqwarna')
motorcycles.append('vespa')
print(motorcycles)
#insert an item in a list
motorcycles.insert(0,'puch')
print(motorcycles)
#delete item in list based on position 
del motorcycles[2]
print(motorcycles)
#delete an item and keep the value for re-use
print(motorcycles.pop(1))
print(motorcycles)
#delete an item based on value is done with the remove() mothod
motorcycles = motorcycles_orig
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

