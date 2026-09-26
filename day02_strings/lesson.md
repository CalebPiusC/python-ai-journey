# Day 2: Strings

A **string** is just text — any characters wrapped in quotes.

## 1. Creating strings
Single or double quotes both work (just be consistent):

```python
name = "Amara"
city = 'Lagos'
```

⚠️ Numbers in quotes are still text, not numbers:

```python
age = "25"   # this is a string, you can't do maths with it
```

## 2. Joining strings (concatenation)
Use `+` to glue strings together:

```python
first = "Ada"
last = "Obi"
full = first + " " + last
print(full)  # shows: Ada Obi
```

Notice we had to add `" "` ourselves — Python doesn't add spaces for you!

## 3. f-strings (the modern, easier way) ⭐
Put an `f` before the quotes, then drop variables inside `{ }`:

```python
name = "Amara"
age = 25
print(f"My name is {name} and I am {age} years old.")
# shows: My name is Amara and I am 25 years old.
```

This is the way you'll use most often. Much cleaner than `+`!

## 4. Useful string tools

```python
word = "  python  "

print(len(word))        # 10 → length (counts EVERYTHING, even spaces!)
print(word.strip())     # "python" → removes spaces from both ends
print(word.upper())     # "  PYTHON  " → ALL CAPS
print(word.lower())     # "  python  " → all small
print(word.replace("o", "0"))  # "  pyth0n  " → swaps letters
```

> Pattern: `variable.method()` — a method is an action the string knows how to do.
> Don't forget the `( )` at the end!

You can also **chain** methods:

```python
print("  python  ".strip().upper())  # shows: PYTHON
```

## 5. Indexing (picking out letters)
Each character has a **position number**, and counting starts at **0**:

```
 P   y   t   h   o   n
 0   1   2   3   4   5
```

```python
word = "Python"
print(word[0])   # shows: P (first letter)
print(word[2])   # shows: t
print(word[-1])  # shows: n (-1 means "last letter")
```

## 6. Quick recap
- Strings are text in quotes: `"hello"`
- `+` joins strings; `f"..."` with `{ }` is cleaner and preferred
- `len()` counts characters (spaces included!)
- Methods: `.strip()`, `.upper()`, `.lower()`, `.replace()`
- Indexing starts at **0**; `[-1]` gets the last character

---
👉 **Now try the 3 exercises in `exercises.py`!**
Run them with: `python exercises.py`
