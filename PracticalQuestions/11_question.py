# Write a python program to remove all the lines that contain the character ‘a’ in a
# file and write it to another file.

with open("sample.txt", "r") as f: 
    lines = f.readlines()

lst = []

for line in lines: 
    if "a" not in line: 
        lst.append(line)

with open("final.txt", "w") as f: 
    f.writelines(lst)