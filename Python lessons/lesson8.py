# Day 8 - Logical operators: and, or, not
is_hot = True
is_sunny = True
is_weekend = False

# and: BOTH sides must be True
if is_hot and is_sunny:
    print("It's hot and sunny - perfect beach day!")

# or: AT LEAST ONE side must be True
if is_hot or is_weekend:
    print("Time to relax!")

# not: flips True to False (and False to True)
if not is_weekend:
    print("It's a weekday - back to Python practice!")
