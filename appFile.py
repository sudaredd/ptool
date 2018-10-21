employee_file = open("employee.txt","r")

#print("read whole file")
#print(employee_file.read());

print("read by line")
for line in employee_file.readlines():
    print(line)

employee_file.close()

employee_file = open("employee.txt","a")
employee_file.write("kelly->Customer sesrvice\n");
employee_file.close();

employee_file = open("employee1.txt","w")
employee_file.write("kelly konvey->Customer sesrvice\n");
employee_file.close();