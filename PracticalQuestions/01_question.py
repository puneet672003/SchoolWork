# Write a python program to search an element in a list and display the frequency of
# element present in list and their location using Linear search by using user defined
# function. [List and search element should be entered by user]

def linearSearch(arr, n): 
    count = 0

    for i in range(len(arr)): 
        if str(arr[i]) == n: 
            print(f"Element fount at : {i}")
            count += 1
    
    print(f"Frequency : {count}")

arr = eval(input("Enter list : "))
n = input("Enter element to search : ")

linearSearch(arr, n)
