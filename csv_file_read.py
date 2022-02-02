import csv

customers = open ('customers.csv','r')

customer_file = csv.reader(customers, delimiter=",")


#to skip a line if the file contains a header record
next(customer_file)

for record in customer_file:
    print("Fname:", record[1])
    print("Lname:", record[2])
    print("Salary:", record[3])
    print("Bonus:", record[4])

    salary =  float(record[3])

    Total_Pay = (Salary + (Salary*Bonus ))
    
    print("Total Pay:",  )


    

    

