# Day 1: Variables & Data Types

## 1. What is a variable?
A **variable** is a named box that stores a value. You create one with the `=` sign
(called *assignment*):

```python
name = "Amara"
age = 25
```

- `name` now holds the text `"Amara"`
- `age` now holds the number `25`

You can see what's inside with `print()`:

```python
print(name)  # shows: Amara
print(age)   # shows: 25
```

Variables can change — that's why they're called *variable*:

```python
age = 26
print(age)  # shows: 26
```

## 2. Naming rules (important!)
1. Names can contain letters, numbers, and underscores: `my_name`, `age2`
2. Names **cannot** start with a number: `2cool` ❌
3. Names are **case-sensitive**: `Age` and `age` are different boxes
4. Use **lowercase with underscores** (called *snake_case*): `favorite_food`
5. Don't use Python keywords: `print`, `if`, `for`, etc.

## 3. The 4 basic data types

| Type | Name | Example | Meaning |
|------|------|---------|---------|
| `int` | Integer | `age = 25` | Whole numbers |
| `float` | Float | `price = 19.99` | Decimal numbers |
| `str` | String | `name = "Amara"` | Text (in quotes) |
| `bool` | Boolean | `is_student = True` | Either `True` or `False` |

Notice:
- Text needs quotes (`" "` or `' '`), numbers don't.
- `True` / `False` start with a **capital letter**, no quotes.

## 4. Checking the type with `type()`
Not sure what's in a box? Ask Python:

```python
score = 95
print(type(score))  # shows: <class 'int'>

price = 19.99
print(type(price))  # shows: <class 'float'>
```

## 5. Quick recap
- `=` **stores** a value in a variable (it does NOT mean "equals" like in maths).
- `print()` **shows** a value on the screen.
- Every value has a **type**: `int`, `float`, `str`, or `bool`.
- `type()` tells you the type.

---
👉 **Now try the 3 exercises in `exercises.py`!**
Run them with: `python exercises.py`
