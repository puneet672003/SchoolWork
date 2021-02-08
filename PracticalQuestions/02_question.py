# Write a python program to search an element in a list and display the frequency of
# element present in list and their location using binary search by using user defined
# function. [List and search element should be entered by user]

def SearchElement (arr, x, l, r): 
    found = []

    def binarySearch(arr, x, l, r): 
        # Check base case 
        if r >= l: 

            mid = l + (r - l) // 2

            if arr[mid] == x: 
                found.append(mid)

            if arr[mid - 1] >= x: 
                binarySearch(arr, x, l, mid-1) 

            if arr[mid + 1] <= x: 
                binarySearch(arr, x, mid + 1, r) 
    
        else: 
            return
            
    arr.sort()
    binarySearch(arr, x, l, r)
    found.sort()
    
    print(f"Frequency : {len(found)}")
    print(f"Indexes : {found}")

arr = eval(input("Enter list : "))
x = int(input("Enter element to search : "))

SearchElement(arr, x, 0, len(arr) - 1)