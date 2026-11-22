#For Loop

fruits = ['Apple', 'Banana', 'Orange']

#Display all element in the list
print('List of fruits:')
for fruit in fruits:
    print(fruit)

#Display all numbers from 0 to 4
print('Count 0-4:')
for i in range(5):
    print('Number:', i)

#Display all numbers from 1-5 range
print('Count 1-5:')
for n in range(1,6):
    print('Number:',n)

#Display all odd number from 1-10 range.
print('Count 1-10 but skip a number:')
for z in range(1,10,2):
    print('Number:', z)

#Display addition in a loop
print('Increment 8 by 1 x5 times:')
num1 = 7
for w in range(5):
    num1 = num1 + 1
    print('Number:', num1)

print('Done')

