##.List
# list=[10,20,30,40]
# sum=0
# for i in list:
#     sum+=i
# print(" Total :",sum) #Output:Total : 100

## Removing duplicate values

# l=[10,20,30,40,10,30]
# new_set=sorted(set(l))
# new_list=list(new_set)
# print(new_list) # Output:[10, 20, 30, 40]

            ##---------list using loops/conditions stmts-----##

# marks = [85, 72, 91, 68, 77]

# print("Marks:", marks)

# highest_marks = marks[0]
# lowest_marks = marks[0]
# length = len(marks)

# for i in marks:
#     if i > highest_marks:
#         highest_marks = i

#     if i < lowest_marks:
#         lowest_marks = i

# print("Highest Marks:", highest_marks)
# print("Lowest Marks:", lowest_marks)
# print("Length:", length)

                ##----indexing----##
# marks = [85, 72, 91, 68, 77]
# print("Highest Marks:",marks[2])
# print("Second Highest:",marks[0])
# print("Third Highest:",marks[4])
# print("Lowest Marks:",marks[3])

               ##-----Negative Indexing-----##

# marks = [85, 72, 91, 68, 77]
# print("Highest Marks:",marks[-3])
# print("Second Highest Marks:",marks[-5])
# print("Third Highest Marks:",marks[-1])
# print("Lowest Marks:",marks[-2])

                       ##-----Slicing-----##

# marks=[85, 72, 91, 68, 77]
# print("Frist Three Numbers :",marks[:3])
# print("Last Two Numbers    :",marks[3:])
# print("Middle Numbers      :",marks[1:4])


             ##--------Step_Function----------##

# numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# ##--print Every Second Element--##
# print(numbers[0:8:2])
# ##---Third_Element----##
# print(numbers[0:8:3])
# ##-----Reverse-----##
# print(numbers[::-1])


                ##--updating_element---##

# marks = [85, 72, 91, 68, 77]
# marks[1]=72
# marks[3]=70
# marks[0:2]=[95,90]
# print(marks)

                 ##----.append()/method---##

# cities = ["Hyderabad", "Vijayawada", "Chennai"]
# cities.append("Nagullanka")
# cities.append("Vizag")
# print(cities)

                ##-----insert()/method------##

# cities = ["Hyderabad", "Vijayawada", "Chennai"]
# cities.insert(1,"Razole")
# cities.insert(2,"Manepalli")
# print(cities)

                 ##---Extend()/method----##

# cities = ["Hyderabad", "Vijayawada"]
# cities.extend(["Nagullanka","Razole","Manepalli"])
# print(cities)

                   ##----Remove()/method------##

# cities = ["Hyderabad", "Vijayawada", "Chennai", "Vizag", "Razole"]
# cities.remove("Chennai")
# print(cities)

                      ##---------pop()/method------##

# cities = ["Hyderabad", "Vijayawada", "Chennai", "Vizag", "Razole"]

# cities.pop(2)

# cities.pop()

# print(cities)

                      ##---------clear()/method-----##

# cities = ["Hyderabad", "Vijayawada", "Chennai", "Vizag"]

# cities.clear()

# print(cities)

                     ##-------index() && count()-------##

# marks = [85, 90, 75, 85, 95, 85, 90]
# print(marks.index(75))
# print(marks.count(90))
# print(marks.count(85))

                     ##-----sort() && reverse ---------##

# ## Ascending Order

# marks = [85, 72, 91, 68, 77]
# marks.sort()
# print("Ascending Order:",marks)

# ## Descending Order

# marks = [85, 72, 91, 68, 77]
# marks.sort(reverse=True)
# print("Descending Order:",marks)

# ## Reverse method

# marks = [85, 72, 91, 68, 77]
# marks.reverse()
# print("Reverse:",marks)

                           ##--------copy()/method-------##

# marks = [85, 72, 91, 68, 77]
# new_marks=marks.copy()
# print(new_marks)
# new_marks[0]=100
# print("New marks:",new_marks)

                      ##---------list Memebership operators-------##

# marks = [85, 72, 91, 68, 77]
# print(85  in marks)
# print(91 in marks)
# print(120 not in marks)
# print(100 in marks)

                      ##-----list using Conditional stmts--------##

# marks = [85, 72, 91, 68, 77]

# if 91 in marks:
#     print("91 is present")

# if 100 not in marks:
#     print("100 is not present")

                         ##----------list looping----------##

# marks = [85, 72, 91, 68, 77]
# total_marks=0
# for mark in marks:
#     total_marks+=mark
#     print("marks:",mark)
# print("Total Marks:",total_marks)   

                     ##------ Filtering a List ----------##

# marks = [85, 72, 91, 68, 77, 54, 96]
# new_list=[]
# for i in marks:
#     if i>75:
#         new_list.append(i)
# print("New list:",new_list)

## method 2

# marks = [85, 72, 91, 68, 77, 54, 96]

# new_list=[i for i in marks if i > 75]

# print(new_list)

## Problem 2:-

# marks = [85, 72, 91, 68, 77]

# new_marks=[i+5 for i in marks]

# print(new_marks)

## Problem 3:-

# marks = [85, 72, 91, 68, 77, 54, 96]

# new_marks=["Pass" if mark>=75 else "Fail" for mark in marks]

# print(new_marks)

## Problem 3:-

# cities = ["Hyderabad", "Chennai", "Vizag", "Razole"]

# new_cities=[city for city in cities if len(city)>6]
# print(new_cities)

                    ##-------  any() and all() ---------##

marks = [85, 72, 91, 68, 77]

result_1=any(mark >90 for mark in marks)
result_2=all(mark >=50 for mark in marks)
result_3=all(mark >=75 for mark in marks)
print(result_1)
print(result_2)
print(result_3)