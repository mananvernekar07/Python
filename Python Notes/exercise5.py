#Unique Employee IDs in the list
employee_id = [101, 101, 102, 103, 103, 102, 101]
unique_employee_id = set(employee_id)
print("Employee IDs")

#Search Employee records
for id in unique_employee_id:
    print(id)

employees = [
    (101,"Alice",50000),
    (102,"Bob",65000),
    (103,"Charlie",45000)
]

search = int(input("Enter Employee ID:"))

for employee in employees:
    if employee[0] == search:
        print("Employee found!")
        print("Employee ID:",employee[0])
        print("Employee Name:",employee[1])
        print("Salary:",employee[2])
        break
else:
    print("Employee not found!")
        
