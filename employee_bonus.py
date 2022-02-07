import csv 
employees = open("EmployeePay.csv", 'r')

employee_file = csv.reader(employees, delimiter= ',')

next(employee_file)

for record in employee_file:
    print ('First Name:', record[1])
    print ('Last Name:', record[2])
    print ('First Name:', record[3])

    Salary = float(record[3])
    bonus = float(record[4])
    bonus = round(Salary * bonus, 2)
    print ("Bonus: $",bonus)
    total_Pay = round((Salary * bonus ) + Salary, 2)

    print ("Total_Pay:", total_Pay)
    input ("Hit Enter to show new employee")


    




