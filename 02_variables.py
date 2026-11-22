# Variables
print("Hello World!")
print()     #print a blank line
message_1 = "This is the study of Variables in Python."   # message = variable
print(message_1)

# Rules for variables
    # letters, numbers, & underscores.  Cannot start w/ number
    # Space is now allowed
    # Avoid using python's commands
    # Avoid lower case L & Upper case O becuz it looks like l & O
    # Suggestion: all variable should be lowercase

message_2 = "I understand variables now"
print(message_2)
print()

message_3 = "That's great!"
message_1 = message_3
print(message_1)

#Strings
string_1 = "This is strings in double quotes."
string_2 = 'AND this is string in single quote.'
string_3 = '"This is a double quote words!"' #words in double quote
string_4 = "The 'Python' language is not a snake." #words in single quote

print()
print(string_1)
print(string_2)
print(string_3)
print(string_4)
print()

name_1 = "jack johnson"
name_2 = "U.S.A"
print(name_1.title())   #change the case of the first letter
print(name_1.upper())   #change all to uppercase
print(name_2.lower())   #change all to lowercase
print()

first_name = "misty"
last_name = "pham"
fullname = f"{first_name} {last_name}"  #f-string. Replace variable in {} as value
print(fullname)
print(fullname.title())

greeting_1 = f"Hello, {fullname.title()}!"
greeting_2 = f'Hello, Mrs. {last_name.title()}!'
print(greeting_1)
print(greeting_2)
print()

#Whitespaces
print("The current languages: ", "Python","\tC++", "\tJavaScript\n")
print("The old languages: \n\tFortran\n\tPascal\n")
print("\tI\tlove\tit.\n")

#Removing spaces
favorite_language = 'C++  '
print("My favorite language is ",favorite_language.rstrip())

#Removing prefixes
url = 'https://www.google.com'
web_address = url.removeprefix('https://')
print()
print(url)
print()
print(web_address)

#integers & float (whole number & Decimal number)
num_1 = int(10)
num_2 = float(10)
num_3 = 5_000_000
num_4, num_5, num_6 = 4, 5, 6
print(num_1)
print(num_2)
print(num_3)
print(num_4)
print(num_5)
print(num_6)

total_1 = num_1 + num_2 + num_4 + num_5 + num_6
mult_1 = num_1 * num_5
div_1 = num_3 / num_1
pwr_1 = num_4 ** num_6

print("Math operations:\n")
print("Add: ", total_1)
print("Multiply: ", mult_1)
print("Division: ", div_1)
print("Exponential of 4^6: ", pwr_1)

import this






