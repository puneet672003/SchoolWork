# Write a Python program to function with key and value, and update value at that key
# in dictionary entered by user.

def updateDict(dict, key, value): 
    if key not in dict.keys(): 
        print("Key does not exist")
    else : 
        dict[key] = value 

myDict = {
    "name": "Puneet", 
    "class": "12 A", 
    "roll no.": "33"
}

key = input("Enter key : ")
value = input("Enter value : ")

updateDict(myDict, key, value)
print(myDict)