##------Tuple Indexing----##

my_tuple=(100,82,73,64,85)
print("Highets marks:",my_tuple[0])
print("Second Highest:",my_tuple[-1])
print("Third Highest:",my_tuple[1])
print("Length:",len(my_tuple))

##------Tuple Slicing-------##

marks = (100, 82, 73, 64, 85)
print("First three: ",marks[:3])
print("Last two:",marks[3:])
print("Middle Numbers:",marks[1:4])
print("Reverse:",marks[::-1])

#-----difference b/w list and tuple

# marks = (100, 82, 73, 64, 85)
# marks[1] = 90
# print(marks) 
#-output("marks[1] = 90 TypeError: 'tuple' object does not support item assignment")

#----tuple count----##

marks = (85, 90, 75, 85, 95, 85, 90)

print("85 Count:", marks.count(85))
print("90 Count:", marks.count(90))
print("75 Index:", marks.index(75))

#------Tuple unpacking---------##

student = ("Chandu", 21, "IT", 7.8)
name,age,branch,cgpa=student
print("Name   :",name)
print("Age    :",age)
print("Branch :",branch)
print("CGPA   :",cgpa)

#-----🧪 Tuple Practice 1 — Student Data------##

student = ("Chandu", 21, "IT", 7.8)
name,age,branch,cgpa=student
print("Name   :",name)
print("Age    :",age)
print("Branch :",branch)
print("CGPA   :",cgpa)

#---------🧪 Practice 2 — Marks-------##

marks = (85, 72, 91, 68, 77)
total=0
for mark in marks:
    total+=mark
print("Total          :",total)
print("No.of Subjects :",len(marks))
print("Highest Marks  :",max(marks))
print("Lowest Marks   :",min(marks))

#------🧪 Practice 3 — Tuple Conversion-----##

marks = [85, 72, 91, 68, 77]
print("Orginal Tuple   :",marks)
new_tuple=tuple(marks)
print("Converted Tuple :",new_tuple)