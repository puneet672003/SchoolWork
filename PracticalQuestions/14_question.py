# Write a python program to create a binary file with roll number, name and marks,
# input a roll number and update the marks.

import pickle

n = int(input("Enter total number of students : "))

data = {}

def read_data(): 
    with open("student_data.bin", "rb") as f: 
        data = pickle.load(f)
    return data

def put_data(data): 
    with open("student_data.bin", "wb") as f: 
        pickle.dump(data, f)

for i in range(1, n+1): 
    print()
    roll_no = int(input(f"{i}) Enter student's roll no. : "))
    name = input(f"{i}) Enter student's name : ")
    marks = float(input(f"{i}) Enter student's marks : "))

    data[roll_no] = { #
        "name": name, 
        "marks": marks
    }
    
put_data(data)

roll_no = int(input("\nEnter roll number to search : "))

data = read_data()
student_info = data.get(roll_no)

if student_info is not None: 
    marks = float(input("Enter new marks : "))

    data[roll_no]["marks"] = marks
    put_data(data)

else : 
    print(f"No data associated with roll no. : {roll_no}")