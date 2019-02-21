# List creation and usage examples
bicycles=['trek','conandale','redline','specialized']
print(bicycles)
print('first item:'+bicycles[0])
print('second item:'+bicycles[1])
print('last item:'+bicycles[-1])
print('-----------------------------------')
print()
# Names example
names=['elif','mert','melisa','harun']
print('Dear '+names[0].title()+',\nAre you coming to class this week?')
print('Dear '+names[1].title()+',\nAre you coming to class this week?')
print('Dear '+names[2].title()+',\nAre you coming to class this week?')
print('Dear '+names[3].title()+',\nAre you coming to class this week?')
print('-----------------------------------')
print()

# Favorite transportation
vehicles=['car','motorcycle','bike']
message="I would like to own a "
print(message+vehicles[0])
print(message+vehicles[1])
print(message+vehicles[2])
print('-----------------------------------')
print()

# Adding value to a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(0,'bmw')
print(motorcycles)
print('-----------------------------------')
print()

# Removing value to a list
motorcycles = ['honda', 'ducati', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)



