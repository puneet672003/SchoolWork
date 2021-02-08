# Write a python program to create a binary file with name and roll number. Search
# for a given roll number and display name, if not found display appropriate message.
import pickle

n = int(input("Enter total number of students : "))

data = {}

for i in range(1, n+1): 
    roll_no = int(input(f"{i}) Enter student's roll no. : "))
    name = input(f"{i}) Enter student's name : ")

    data[roll_no] = { #
        "name": name
    }
    
with open("student_data.bin", "wb") as f: 
    pickle.dump(data, f)

roll_no = int(input("Enter roll number to search : "))

with open("student_data.bin", "rb") as f: 
    data = pickle.load(f)
    student_info = data.get(roll_no)

if student_info is not None: 
    name = student_info["name"]
    print(f"Name of the student : {name}")
else : 
    print(f"Cannot find any information of student having roll number : {roll_no}")
