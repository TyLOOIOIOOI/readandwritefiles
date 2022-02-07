import csv

customers = open ('customers.csv','r')

outfile = open('customer_country.csv', 'w')

customer_file = csv.reader(customers, delimiter=",")


n=-1
for record in customer_file:
    #print("First Name:", record[1],"Last Name:", record [2], "Country:", record[4] ) 
    outfile.write(record[1] + "," + record [2] + "," + record[4] + "\n")

    n += 1
print("Costomer Count:", n)

outfile.close()