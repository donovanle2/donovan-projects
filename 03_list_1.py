# List 01
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])

print(bicycles[1].title())

print(bicycles[-1])

message = f"My first bicycle was a {bicycles[3].title()}"
message2 = f"{bicycles[0]} {bicycles[1]} {bicycles[2]} {bicycles[3]}"
print(message)
print('-------------------------------------')
print(message2)
print('-------------------------------------')

fruits = ['apple', 'banana', 'orange']

print(fruits[0])
print(fruits[-1])

fruits[1] = 'mango'

print(fruits[1])
print(fruits)

fruits.append('lemon')

print(fruits)

del fruits[1]
print(fruits)
fruits.append('mango')
fruits.append('apple')

print(fruits)


index = 3

print(fruits[index])

fruits.remove('mango')

print(fruits)

fruits.append('mango')
print(fruits)
print(fruits)
fruits[0] = 'pear'
print(fruits)
fruits.insert(0, 'pear')
print(fruits)
fruits.pop(0)
print(fruits)

fruits.insert(-1, 'Jackson')
print(fruits)


list_length = len(fruits)
print('Length of list', list_length)