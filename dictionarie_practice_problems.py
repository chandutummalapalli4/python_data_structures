# my_dict={'Name:''Harry','Age:''12','House:''Gryffindor'}
# print(my_dict)

#    #----Accessing the values in the dictionary----#

# my_dict={'name': 'Harry', 'age': 11, 'house': 'Gryffindor'}

# name_value = my_dict['name']
# print(name_value)
# age_value = my_dict['age']
# print(age_value)
# house_value = my_dict['house']
# print(house_value)

#      ##----Adding element-----##
# d={'Name': 'Chandu','Age': '21','Department': 'IT'}
# d['Gender'] = 'male'
# print("Updated dict:",d)

#     #----------Adding & Updating Values----------##

# student = {
#     "name": "Chandu",
#     "age": 21,
#     "branch": "IT"
# }

# student["city"] = "Nagullanka"
# student["age"] = 22

# print(student)

# #problem 2:-
# student={ 
#     "name":"Ram",
#     "age" :"21",
#     "branch":"IT",
#     }
# student["branch"]="CSE"
# student["Gender"]="Male"
# print(student)

#   ##------clear() && pop() && delete()-------##
# student={ 
#     "name":"Ram",
#     "age" :21,
#     "branch":"IT",
#     "Gender":"Male",
#     "Cgpa":7.72,
# }

# ##----pop()-method-----##
# student.pop("Gender")
# print(student)
# ##----delete()-method---##
# del student["branch"]
# print(student)
# ##----clear()-method----##
# student.clear()
# print(student)

# #---🟢 Next: Dictionary Membership---##

# student = {
#     "name": "Ram",
#     "age": 21,
#     "branch": "IT"
# }

# print("city" in student)
# print("age" in student)
# print("branch" not in student)

# #----keys(), values(), items()---##

# student = {
#     "name": "Ram",
#     "age": 21,
#     "branch": "IT"
# }

# print(student.keys())
# print(student.values())
# print(student.items())

# #-----looping------##

# student = {
#     "name": "Ram",
#     "age": 21,
#     "branch": "IT",
#     "cgpa": 7.72
# }
# for key,value in student.items():
#     print(key,":",value)

   ##---get()----##

# student = {
#     "name": "Ram",
#     "age": 21,
#     "branch": "IT",
#     "cgpa": 7.72
#     }
# print(student.get("name"))
# print(student.get("city"))

##---problem-1---##

# student = {
#     "name": "Ram",
#     "age": 21,
#     "branch": "IT"
# }
# print(student.get("name"))
# print(student.get("city","Not avaliable"))

##---pratice question on dict---##

# student = {
#     "name": "Chandu",
#     "age": 21,
#     "branch": "IT",
#     "cgpa": 7.72
# }
# for key,values in student.items():
#     print(key,":",values)
# student["city"]="Razole"
# print(student.get("name"))
# student.pop("age")
# student["cgpa"]=8.0
# print("Upadted dict:",student)

##---challenge---##

# student = {
#     "name": "Chandu",
#     "age": 21,
#     "branch": "IT",
#     "cgpa": 7.72
# }
# for key in student.keys():
#     print("Keys:",key)
# for values in student.values():
#     print(values)

         ##--------Nested dictinarys-------##
# students = {
#     "student1": {
#         "name": "Chandu",
#         "age": 21,
#         "branch": "IT"
#     },
#     "student2": {
#         "name": "Ravi",
#         "age": 22,
#         "branch": "CSE"
#     }
# }
# print(students["student1"]["name"])
# print(students["student1"]["age"])
# print(students["student1"]["branch"])

# ##------student 2-------##

# print(students["student2"]["name"])
# print(students["student2"]["age"])
# print(students["student2"]["branch"])

# ##-----updating-----##

# students["student1"]["age"] = 22
# students["student2"]["branch"] = "IT"
# students["student2"]["city"] = "Hyderabad"

# print(students)

##----🎯 Next: Practical Dictionary Problem-----##

# students = {
#     "student1": {
#         "name": "Chandu",
#         "marks": 85
#     },
#     "student2": {
#         "name": "Ravi",
#         "marks": 92
#     },
#     "student3": {
#         "name": "Kiran",
#         "marks": 78
#     }
# }

# print(students["student1"]["name"])
# print(students["student1"]["marks"])

# print(students["student2"]["name"])
# print(students["student2"]["marks"])

# print(students["student3"]["name"])
# print(students["student3"]["marks"])

# # Update
# students["student1"]["marks"] = 90
# students["student3"]["branch"] = "IT"

# print(students)

           ##----nested dict looping---##
students = {
    "student1": {
        "name": "Chandu",
        "marks": 85
    },
    "student2": {
        "name": "Ravi",
        "marks": 92
    },
    "student3": {
        "name": "Kiran",
        "marks": 78
    }
}
# for key ,details in students.items():
#     print(key,":",details)
for key, details in students.items():
    print(key)
    print("Name :", details["name"])
    print("Marks:", details["marks"])
