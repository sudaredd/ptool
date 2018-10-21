from appClass import student

student1 = student("Pat","12",3.1,"computers")
student2 = student("Steve","11",3.6,"electronics")

print(student1.name)
print(student2.major)

print(student1.on_honour_roll())
print(student2.on_honour_roll())