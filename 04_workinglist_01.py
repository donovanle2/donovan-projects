#Working with list

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)

for i in magicians:
    print(f"{i.title()}, That was a great trick")
    print(f"I can't wait to see your next trick, {i.title()}.\n")

print("Thank you everyone. That was a great show.\n")


numbers = range(1,6)
print(numbers)

numbers = list(range(1,6))
print(numbers)

squares = []
squares2 = []
for j in range(1,11):
    square = j**2
    squares.append(square)
print(squares)

for w in range(1,11):
    squares2.append(w**2)
print(squares2)

digits = list(range(1,10))
print(digits)
minimum_no = min(digits)
maximum_no = max(digits)
total_sum = sum(digits)
print('minimum:', minimum_no)
print('maximum:', maximum_no)
print('Total:', total_sum)
