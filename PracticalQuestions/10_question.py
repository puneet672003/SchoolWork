# Write a python program to read and display file content line by line with each word  separated by #. 

with open("sample.txt", "r") as f: 
    lines = f.readlines()
    
for line in lines: 
    words = line.split()
    for word in words: 
        print(word, end = "#")
    print()