# Write a python program to read characters from keyboard one by one, all lower
# case letters gets stored inside a file “LOWER”, all uppercase letters gets stored inside a
# file “UPPER” ,and all other characters get stored inside “OTHERS”

string = input("Enter string : ")

upper = []
other = []

for char in string: 
    if char.isupper(): 
        upper.append(char)
    else : 
        other.append(char)

with open("upper.txt", "w") as f: 
    f.writelines(upper)

with open("other.txt", "w") as f: 
    f.writelines(other)