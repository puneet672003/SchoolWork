# Write a python program to create a CSV file with empid, name and mobile no. and
# search empid, update the record and display the records.
import csv
from pickle import dump 

def create_file(): 
    fields = ["empid", "name", "mobile_no"]

    with open("employee_data.csv", "w", newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    
def insert_row(row): 
    with open("employee_data.csv", "a", newline = "\n") as f: 
        writer = csv.writer(f)
        writer.writerow(row)

def get_data(format = "dict"): 
    with open("employee_data.csv", "r") as f: 
        data = csv.reader(f)
        fields = next(data)
        rows = []

        for row in data: 
            rows.append(row)
            
    return fields, rows

def update_record(empid, to_update, value): 
    if to_update == "name": 
        index = 1
    elif to_update == "mobile_no": 
        index = 2
    else : 
        raise Exception("Wrong arguement provided to update")

    fields, rows = get_data()
    for row in rows: 
        if row[0] == empid: 
            row[index] = value 

    with open("employee_data.csv", "w", newline = "\n") as f: 
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerows(rows)

def get_employee_data(empid): 
    fields, rows = get_data()
    for row in rows : 
        if row[0] == empid: 
            return row
    else : 
        return 

def print_records(): 
    fields, rows = get_data(format = "list")
    print(fields)

    for row in rows: 
        print(row)

print("Type 1 to create a csv file.")
print("Type 2 insert a row in csv file.")
print("Type 3 to update an existing row.")
print("Type 4 to prin all the records on screen.")

opt = int(input("\n: "))

if opt == 1: 
    create_file()

if opt == 2: 
    row = []

    for i in ["empid", "name", "mobile no."]: 
        row.append(input(f"Please type {i} of new employee : "))

    insert_row(row)

if opt == 3: 
    empid = input("Please enter empid of employee : ")
    emp_data = get_employee_data(empid)

    if emp_data is not None: 
        name = emp_data[1]
        mobile = emp_data[2]

        print(f"Name : {name}")
        print(f"Mobile no. : {mobile}")
        print("------------------------------")
        print("What Do you want to update ? ")
        print("Type 1 to update name")
        print("Type 2 to update mobile no.")
        print("------------------------------")

        opt2 = int(input(": "))

        if opt2 == 1: 
            new = input("Enter new name : ")
            update_record(empid, "name", new)

        elif opt2 == 2: 
            new = input("Enter new mobile no. : ")
            update_record(empid, "mobile_no", new)


if opt == 4: 
    print_records()

else : 
    print("Wrong arguement given!!")