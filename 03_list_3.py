# Working with List

#Create a list
animals = ['Dog', 'Cat', "Rabbit", 'Hampster']

#1st anmial on the list
print('First animal on the list is', animals[0])

#Last animal on the list
print ('Last animal on the list is', animals[-1])

#Change Hampster to mouse
animals[3] = 'Mouse'
print ('Change "hampster" to "mouse"')
print(animals)

#Add new animal to the end of the list
animals.append('Turtle')
print('New animal is', animals[-1])
print(animals)

#Add new animal in the middle of the list
animals.insert(1, 'Goldfish')
print('Another new animal is', animals[1])
print(animals)

#Remove goldfish out of the list
animals.remove('Goldfish')
print('Removing goldfish from the list')
print(animals)

#Remove or pop the last item on the list
print('The animals got pop is:', animals.pop())
print(animals)

#Sort animals alphabetically (A-Z)
animals.sort()
print('Sorting animals alphabetically (A-Z):')
print(animals)

#Sort animals alphabetically (Z-A)
animals.sort(reverse=1)
print('Sorting animals alphabetically (Z-A): ')
print(animals)

#Temporarily sort animals (A-Z) for displace
print('Here is the actual animals list')
print(animals)
print('Here is the animals list that temporary sorted for display')
print(sorted(animals))
print('Here is the animals list back to normal')
print(animals)

#Displace animal in reverse order
print('The original animal list')
print(animals)
animals.reverse()
print('The animal list in reverse order')
print(animals)

#count how many animals in the list
print('Total animals in the list are', len(animals))


