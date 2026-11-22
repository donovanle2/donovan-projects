#Working with list - Tuples = immutable list (e.g cannot change)

#Create a tuple
dimensions = (200, 50)

#Display the tuple
print(dimensions[0])
print(dimensions[1])

#Display all element in tuple
print('All elements in tuple:\n')
for i in dimensions:
    print(i,'\n')

#Overwrite tuple

dimensions = (200, 50)
print('\nOriginal Tuple:')
for i in dimensions:
    print(i)

dimensions = (300, 500)
print('\nTuple after being modified:')
for j in dimensions:
    print(j)


