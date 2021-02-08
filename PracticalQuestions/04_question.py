# Write a Python program input n numbers in tuple and pass it to function to count
# how many even and odd numbers are entered.

def count_EvenOdd(arr): 
    even_count = 0
    odd_count = 0 

    for i in arr: 
        if i%2 == 0: 
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

tup = eval(input("Enter tuple : "))
event_count, odd_count = count_EvenOdd(tup)

print(f"Event counts : {event_count}")
print(f"Odd counts : {odd_count}")