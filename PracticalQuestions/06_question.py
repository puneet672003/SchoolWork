# Write a Python program to pass a string to a function and count how many vowels  present in the string.  

def count_vowels(string): 
    vowels = ["a" ,"e", "i", "o", "u"]
    count = 0

    for char in string: 
        if char.lower() in vowels: 
            count += 1

    return count

print(f"Total vowels : ", count_vowels(input("Enter string : ")))