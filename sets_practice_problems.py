# empty set
empty_set = set()
#Creating a set with elements
fruits = {'apple', 'banana', 'grape'}
print(fruits)
# Creating a set from a list
numbers = set([1, 2, 3, 4, 5])

#                   ##--- Set methods  ----##
# 1.Add
set={1,2,3,4,5}
set.add(7)
print("Updated Set :",set)
# 2.remove
my_set={1,2,3,8,9}
my_set.remove(3)
print("Updated Set:",my_set)

#                   ## --- Set Operation --- ##
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2) 
print(union_set) # Output: (1, 2, 3, 4, 5)
intersection_set = set1.intersection(set2)
print(intersection_set) # Output: (3)
difference_set = set1.difference (set2) 
print(difference_set)
# Output: (1, 2)
symmetric_difference_set = set1.symmetric_difference (set2)
print(symmetric_difference_set) # Output: (1, 2, 4, 5)

#                  ##---- Set Memebership -----##
set_1={1,2,3,4}

print(2 in set_1)  ## Output:(True)
print(23 in set_1) ## Output:(False)
print(len(set_1))  ## Output:(4)

#                        ##-----------practice-session-------##

numbers = {10, 20, 30, 40, 20, 30}

print(numbers)
print(type(numbers))
print(len(numbers))

# #----problem 2---------##

cities = {"Hyderabad", "Chennai", "Vizag", "Hyderabad", "Chennai"}

print(cities)
print(len(cities))

# # 3.

cities = {"Hyderabad", "Chennai", "Vizag"}

cities.add("Razole")

print(cities)

# # 4.

set={"10","20","30","40"}
set.add("20")
set.add("200")
print(set)  ##.output-{'200', '30', '20', '40', '10'}

##---remove()----##

numbers = {10, 20, 30, 40}
numbers.remove(20)
print(numbers)

##----discard---##
numbers = {10, 20, 30, 40}

numbers.discard(200)

print(numbers)

##----pop()-----##
numbers = {10, 20, 30, 40}

removed = numbers.pop()

print("Removed:", removed)
print("Set:", numbers)

## List.pop() → predictable by index
## Set.pop()  → arbitrary element

##----problem--3

cities = {"Hyderabad", "Chennai", "Vizag", "Razole"}
cities.remove("Chennai")
cities.add("Vijayawada")
cities.discard("Delhi")
print(cities)
cities.clear()
print(cities)

##----memebership in sets----##

cities = {"Hyderabad", "Chennai", "Vizag"}

print("Hyderabad" in cities)
print("Delhi" in cities)
print("Delhi" not in cities)

#🚀  Set Operations. 

##🟢 1. Union

numbers_1={10,20,30,40}
numbers_2={200,30,40,50}
result=numbers_1.union(numbers_2)
print(result) 

##--output-{40, 200, 10, 50, 20, 30}

##🟢 2.Intersection

urban={"Nagullanka","Razole","Manepalli","Peddapatanam"}
rular={"Razole","Tatipaka","Nagullanka","Amalapuram"}
result=urban.intersection(rular)
print(result) 

##--output-{'Nagullanka', 'Razole'}

##🟢 3.Difference

# #Difference finds elements that exist in the first set but not in the second set.

urban = {"Nagullanka", "Razole", "Manepalli", "Peddapatanam"}
rural = {"Razole", "Tatipaka", "Nagullanka", "Amalapuram"}
result = urban.difference(rural)
print(result) 

##output:-{'Manepalli', 'Peddapatanam'}

##🟢 4.Symmetric Differencet 
#returns elements that are in either set, but NOT in both.

urban = {"Nagullanka", "Razole", "Manepalli"}
rural = {"Razole", "Tatipaka", "Amalapuram"}

result = urban.symmetric_difference(rural)

print(result)
## output-{'Amalapuram', 'Manepalli', 'Nagullanka', 'Tatipaka'}

                          ##--------[practice-session]-------##
1.
python_students = {"Chandu", "Ravi", "Kiran", "Arjun"}
sql_students = {"Ravi", "Kiran", "Priya", "Arjun"}
result=python_students.intersection(sql_students)
print(result)
## output={'Arjun', 'Kiran', 'Ravi'}

2.
python_students = {"Chandu", "Ravi", "Kiran", "Arjun"}
sql_students = {"Ravi", "Kiran", "Priya", "Arjun"}
result=python_students.difference(sql_students)
print(result)
## Output={'Chandu'}

3.
python_students = {"Chandu", "Ravi", "Kiran", "Arjun"}
sql_students = {"Ravi", "Kiran", "Priya", "Arjun"}
result=python_students.union(sql_students)
print(result)
## Output={'Ravi', 'Priya', 'Arjun', 'Chandu', 'Kiran'}

4.
python_students = {"Chandu", "Ravi", "Kiran", "Arjun"}
sql_students = {"Ravi", "Kiran", "Priya", "Arjun"}
result=sql_students.difference(python_students)
print(result)
## Output={'Priya'}

5.
morning_shift = {"Chandu", "Ravi", "Kiran", "Arjun"}
evening_shift = {"Ravi", "Priya", "Arjun", "Suresh"}
## Find all employees who worked in at least one shift.
result=morning_shift.union(evening_shift)
print(result)
## Output={'Ravi', 'Priya', 'Kiran', 'Chandu', 'Suresh', 'Arjun'}

6.
students_python = {"Chandu", "Ravi", "Kiran", "Arjun", "Meena"}
students_sql = {"Ravi", "Arjun", "Priya", "Meena"}
students_excel = {"Kiran", "Arjun", "Meena", "Suresh"}

# 1. Students who know both Python and SQL
both_python_sql = students_python & students_sql
print("1. Python and SQL:", both_python_sql)

# 2. Students who know Python but not SQL
python_not_sql = students_python - students_sql
print("2. Python but not SQL:", python_not_sql)

# 3. Students who know at least one of the three
at_least_one = students_python | students_sql | students_excel
print("3. At least one:", at_least_one)

# 4. Students who know exactly one of the three
exactly_one = (
    (students_python - students_sql - students_excel)
    | (students_sql - students_python - students_excel)
    | (students_excel - students_python - students_sql)
)

print("4. Exactly one:", exactly_one)

##--Output:-
# 1. Python and SQL: {'Ravi', 'Meena', 'Arjun'}
# 2. Python but not SQL: {'Kiran', 'Chandu'}
# 3. At least one: {'Arjun', 'Priya', 'Ravi', 'Chandu', 'Meena', 'Suresh', 'Kiran'}
# 4. Exactly one: {'Chandu', 'Suresh', 'Priya'}

         ##-------------Final Challenge----------##
         
python = {"Chandu", "Ravi", "Kiran", "Arjun", "Meena"}
sql = {"Ravi", "Arjun", "Priya", "Meena"}
excel = {"Kiran", "Arjun", "Meena", "Suresh"}

all_students = {
    "Chandu", "Ravi", "Kiran", "Arjun",
    "Meena", "Priya", "Suresh", "Rahul"
}

# 1. Students who know all three skills
all_three = python & sql & excel
print("1. All three:", all_three)

# 2. Python and Excel but not SQL
python_excel_not_sql = (python & excel) - sql
print("2. Python and Excel but not SQL:", python_excel_not_sql)

# 3. SQL or Excel but not Python
sql_or_excel_not_python = (sql | excel) - python
print("3. SQL or Excel but not Python:", sql_or_excel_not_python)

# 4. Students who know none of the three
known_students = python | sql | excel
none = all_students - known_students
print("4. None of the three:", none)

# 5. Total number of unique students
unique_students = python | sql | excel
print("5. Total unique students:", len(unique_students))