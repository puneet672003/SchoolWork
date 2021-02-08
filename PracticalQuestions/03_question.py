# Write a python program to pass list to a function and double the odd values and half
# even values of a list and display list element after changing.

def halfEven_doubleOdd(arr): 
    for i in range(len(arr)): 
        if arr[i] % 2 == 0: 
            arr[i] = arr[i]/2
        else :
            arr[i] = arr[i]*2
    
lst = eval(input("Enter list : "))
halfEven_doubleOdd(lst)

print(f"Final list : {lst}")