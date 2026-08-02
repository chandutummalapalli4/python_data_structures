# 🐍 Python Lists Practice

> A hands-on Python learning module focused on understanding and practicing **Lists** through coding exercises, loops, conditions, list methods, filtering, and list comprehensions.

---

# 🎯 Module Goal

This module documents my practical learning journey with **Python Lists**.

I practiced Lists using marks, numbers, and city-based examples to understand how to:

* Store multiple values
* Access and modify elements
* Add and remove data
* Search and count values
* Sort and reverse data
* Copy lists
* Process lists using loops and conditions
* Filter and transform data
* Use list comprehensions
* Apply `any()` and `all()`

The main goal is to build strong Python data-structure fundamentals before moving toward **Tuples, Dictionaries, Sets, NumPy, and Pandas**.

---

# 📚 Topics Covered

## 1️⃣ Creating Lists

Practiced creating lists containing numbers and strings.

```python
marks = [85, 72, 91, 68, 77]

cities = ["Hyderabad", "Vijayawada", "Chennai"]
```

---

## 2️⃣ List Sum Using Loops

Practiced calculating the total of list values using a `for` loop.

```python
numbers = [10, 20, 30, 40]

total = 0

for i in numbers:
    total += i

print("Total:", total)
```

Output:

```text
Total: 100
```

---

## 3️⃣ Removing Duplicate Values

Practiced removing duplicate values using `set()` and converting the result back into a list.

```python
numbers = [10, 20, 30, 40, 10, 30]

new_set = sorted(set(numbers))
new_list = list(new_set)

print(new_list)
```

Output:

```text
[10, 20, 30, 40]
```

---

# 🔢 Indexing

Practiced accessing elements using positive indexes.

```python
marks = [85, 72, 91, 68, 77]

print(marks[0])
print(marks[2])
print(marks[4])
```

---

# 🔄 Negative Indexing

Practiced accessing elements from the end of a list.

```python
marks = [85, 72, 91, 68, 77]

print(marks[-1])
print(marks[-2])
print(marks[-3])
```

---

# ✂️ List Slicing

Practiced extracting sections of a list.

```python
marks = [85, 72, 91, 68, 77]

print(marks[:3])
print(marks[3:])
print(marks[1:4])
```

---

# ⏭️ Slicing with Steps

Practiced selecting elements using a step value.

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[0:8:2])
print(numbers[0:8:3])
print(numbers[::-1])
```

Covered:

* Every second element
* Every third element
* Reversing a list using slicing

---

# ✏️ Updating List Elements

Practiced changing individual elements and multiple elements using slicing.

```python
marks = [85, 72, 91, 68, 77]

marks[1] = 72
marks[3] = 70
marks[0:2] = [95, 90]

print(marks)
```

---

# ➕ Adding Elements

## `append()`

Adds an element to the end of a list.

```python
cities.append("Nagullanka")
cities.append("Vizag")
```

## `insert()`

Adds an element at a specific index.

```python
cities.insert(1, "Razole")
cities.insert(2, "Manepalli")
```

## `extend()`

Adds multiple elements to a list.

```python
cities.extend(["Nagullanka", "Razole", "Manepalli"])
```

### Difference

```text
append() → Add an element at the end
insert() → Add an element at a specific position
extend() → Add multiple elements
```

---

# ➖ Removing Elements

## `remove()`

Removes an element using its value.

```python
cities.remove("Chennai")
```

## `pop()`

Removes an element using its index.

```python
cities.pop(2)
```

Calling `pop()` without an index removes the last element.

```python
cities.pop()
```

## `clear()`

Removes all elements from the list.

```python
cities.clear()
```

Result:

```text
[]
```

---

# 🔍 `index()` and `count()`

## `index()`

Finds the position of a value.

```python
marks = [85, 90, 75, 85, 95, 85, 90]

print(marks.index(75))
```

## `count()`

Counts how many times a value appears.

```python
print(marks.count(90))
print(marks.count(85))
```

---

# 📊 Sorting and Reversing

## Ascending Order

```python
marks = [85, 72, 91, 68, 77]

marks.sort()

print(marks)
```

Result:

```text
[68, 72, 77, 85, 91]
```

## Descending Order

```python
marks.sort(reverse=True)
```

Result:

```text
[91, 85, 77, 72, 68]
```

## Reverse Order

```python
marks.reverse()
```

### Important Difference

```text
sort()              → Sorts values
sort(reverse=True)  → Sorts in descending order
reverse()           → Reverses the current order
```

---

# 📋 Copying Lists

Practiced creating a separate copy using `copy()`.

```python
marks = [85, 72, 91, 68, 77]

new_marks = marks.copy()

new_marks[0] = 100

print("New marks:", new_marks)
```

This helps understand the difference between an independent list copy and simply assigning another variable to the same list.

---

# 🔎 Membership Operators

Practiced:

* `in`
* `not in`

Example:

```python
marks = [85, 72, 91, 68, 77]

print(91 in marks)
print(100 not in marks)
```

These operators are useful for checking whether data exists inside a collection.

---

# 🔀 Lists with Conditional Statements

Practiced using membership checks with `if`.

```python
marks = [85, 72, 91, 68, 77]

if 91 in marks:
    print("91 is present")

if 100 not in marks:
    print("100 is not present")
```

---

# 🔁 Looping Through Lists

Practiced processing each list element using a `for` loop.

```python
marks = [85, 72, 91, 68, 77]

total_marks = 0

for mark in marks:
    total_marks += mark

print("Total Marks:", total_marks)
```

This builds the foundation for performing calculations on collections of data.

---

# 📈 Finding Highest and Lowest Values

Practiced finding the highest and lowest marks manually using loops and conditions.

```python
marks = [85, 72, 91, 68, 77]

highest_marks = marks[0]
lowest_marks = marks[0]

for mark in marks:

    if mark > highest_marks:
        highest_marks = mark

    if mark < lowest_marks:
        lowest_marks = mark

print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
```

Also practiced finding the length of a list using:

```python
length = len(marks)
```

---

# 🔎 Filtering a List

Practiced filtering values based on a condition.

```python
marks = [85, 72, 91, 68, 77, 54, 96]

new_list = []

for mark in marks:
    if mark > 75:
        new_list.append(mark)

print("New list:", new_list)
```

Result:

```text
[85, 91, 77, 96]
```

---

# ⚡ List Comprehension

Practiced converting traditional list-processing logic into concise list comprehensions.

## 1. Filtering

```python
new_list = [i for i in marks if i > 75]
```

## 2. Transformation

Added `5` to every mark:

```python
new_marks = [i + 5 for i in marks]
```

## 3. Conditional Transformation

Classified marks as Pass or Fail:

```python
new_marks = [
    "Pass" if mark >= 75 else "Fail"
    for mark in marks
]
```

## 4. Filtering Strings

Filtered cities based on their name length:

```python
cities = ["Hyderabad", "Chennai", "Vizag", "Razole"]

new_cities = [
    city for city in cities
    if len(city) > 6
]
```

---

# 🧠 `any()` and `all()`

Practiced checking conditions across list values.

## `any()`

Checks whether at least one value satisfies the condition.

```python
marks = [85, 72, 91, 68, 77]

result = any(mark > 90 for mark in marks)

print(result)
```

## `all()`

Checks whether every value satisfies the condition.

```python
result = all(mark >= 50 for mark in marks)

print(result)
```

Also practiced checking whether all marks meet a higher condition:

```python
result = all(mark >= 75 for mark in marks)
```

### Difference

```text
any() → At least one condition is True
all() → Every condition must be True
```

---

# 🧪 Practice Areas

The practice file covers:

* List creation
* List calculations
* Duplicate removal
* Indexing
* Negative indexing
* Slicing
* Step slicing
* Updating elements
* `append()`
* `insert()`
* `extend()`
* `remove()`
* `pop()`
* `clear()`
* `index()`
* `count()`
* `sort()`
* `reverse()`
* `copy()`
* Membership operators
* Conditional statements
* Loops
* Highest and lowest values
* Filtering
* List comprehension
* `any()`
* `all()`

---

# 📊 Data Analyst Connection

Learning Lists is important because it develops the fundamental skills required for handling collections of data.

The learning progression is:

```text
Python Lists
     ↓
Loops & Conditions
     ↓
Filtering & Transformation
     ↓
List Comprehension
     ↓
NumPy Arrays
     ↓
Pandas Series
     ↓
Pandas DataFrames
     ↓
Data Cleaning & Analysis
```

The filtering and transformation techniques practiced here will become especially useful when working with **Pandas**.

---

# 📁 File Structure

```text
Python-Data-Structures/
│
├── Lists/
│   ├── list_practice_problems.py
│   └── README.md
│
└── README.md
```

---

# 🚀 Learning Progress

```text
🐍 Python Lists

✅ Creating Lists
✅ Sum Using Loops
✅ Removing Duplicates

✅ Indexing
✅ Negative Indexing
✅ Slicing
✅ Step Slicing
✅ Updating Elements

✅ append()
✅ insert()
✅ extend()

✅ remove()
✅ pop()
✅ clear()

✅ index()
✅ count()

✅ sort()
✅ reverse()
✅ copy()

✅ Membership Operators
✅ Conditional Statements
✅ Looping Through Lists

✅ Highest & Lowest Values
✅ List Filtering

✅ List Comprehension
   ✅ Filtering
   ✅ Transformation
   ✅ if / else
   ✅ String Filtering

✅ any()
✅ all()
```

---

# 🎯 Next Topic

With the important List concepts completed, the next Data Structures topic is:

## 🟢 Tuples

Upcoming concepts:

* Creating Tuples
* Tuple Indexing
* Tuple Slicing
* `count()`
* `index()`
* Tuple Unpacking
* Immutability
* List vs Tuple
* Practical Examples

After Tuples:

```text
Lists ✅
   ↓
Tuples 🔜
   ↓
Dictionaries
   ↓
Sets
   ↓
Data Structures Mini Project
```

---

# 💡 Learning Approach

My learning process is:

```text
Learn
  ↓
Practice
  ↓
Solve Problems
  ↓
Apply Concepts
  ↓
Build Projects
  ↓
Review
  ↓
Move Forward
```

I focus on understanding concepts through hands-on coding rather than only learning theory.

---

# 👨‍💻 Author

**Chandu Tummalapalli**

🎯 Aspiring Data Analyst
🐍 Python Programmer
📊 Project-Based Learner

> **"Strong fundamentals build strong professionals."**

> **Learn → Practice → Build → Improve → Repeat**
