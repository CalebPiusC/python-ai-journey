# Day 1 - Variables and data types

# --- Part 1: My first variables ---
name = "caleb"
age = 18
favourite_food = "jellof rice"
print(name)
print(age)
print(favourite_food)

# --- Part 2: Checking types with type() ---
a = 10
b = 3.5
c = "python"
print(type(a))
print(type(b))
print(type(c))

# --- Part 3: The 4 basic data types ---
age = 25            # int - whole number
price = 19.99       # float - decimal number
name = "Amara"      # str - text (needs quotes!)
is_student = True   # bool - True or False (capital T/F, no quotes)

print(type(age))         # <class 'int'>
print(type(price))       # <class 'float'>
print(type(name))        # <class 'str'>
print(type(is_student))  # <class 'bool'>

# --- Part 4: Fun with print() ---
print('0----')
print(' ||||')
print('*' * 10)

# --- Part 5: Variables can change ---
price = 10
price = 20  # price is now 20 (the old value 10 is gone)
rating = 4.9
is_published = False
print(price)

full_name = 'john smith'
age = 20
is_new = True  # FIXED: this line had no value, which crashed the program
print(full_name)
print(age)
print(is_new)

# --- Part 6: Getting input from the user ---
name = input('What is your name? ')
print('Hi ' + name)  # FIXED: added the missing space after Hi
