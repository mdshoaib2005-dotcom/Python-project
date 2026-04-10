#Typecasting = The process of converting a variable from one data type to another
#              str(), int(), float(), bool()

name = "Shoaib"
age = 21
cgpa = 8.07
is_student = True

print(type(age))                        #type() is used to find the datatype of the variable
print(type(name))
print(type(cgpa))


age = float(age)
print(age)
print(type(age))

age = str(age)
print(type(age))
print(age)

name = bool(name)                      # this will output always true until there are no string written inside quotes

print(name)