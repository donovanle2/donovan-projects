# Study Notes on "List"

fruits = ['Apple', "Orange", 'Pear']        # Create a list
names = []                                  # Create a blank list

print(fruits)                               # Display the list

print(fruits[1])                            # Display element 2 on the list

fruits.sort()                               # Organize element in list alphabetically

print(sorted(fruits))                      # Display sorted list temporary

fruits.reverse()                            # Reverse the order of element in the list
fruits.reverse()                            # 2nd time to restore original order

fruits[2] = 'Mango'                         # Modify element of the list

fruits.append('Cherry')                     # Add element to the end of list

fruits.insert(2, 'Lemon')                   # Add element of the list at position 2

fruits.remove('Cherry')                     # Remove element 2 from the list

fruits.pop()                                # Remove the last item from the list

fruits.pop(1)                               # Remove & displacy element 2 from the list

del fruits[1]                               # Remove element 2 from of the list

print(fruits)

