#If Statement

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        

car = 'Audi'
print(car == 'audi')

print(car.lower() == 'audi')
print('\n')

topping = input("Enter your favorite topping: ")
if topping.lower() != 'anchovies':
    print('Hold the anchovies!\n')
else:
    print("Ah shit! We don't have it!\n")

age = int(input("Enter your age: "))
if age >= 13 and age < 18:
    print("You're a teenager!\n")
elif age >= 18:
    print("You're an adult!\n")
else:
    print("You are a child!\n")