# Write a Python program to create Lpush( ) and Lpop( ) function to do push and
# pop operation on a stack using a list e.g. take a student information and push and pop
# the details.

stack = []
maxSize = 10
top = -1

def Lpush(element): 
    global top
    global maxSize

    if maxSize == top: 
        print("Stack Overflow!!")
    else : 
        stack.append(element)
        top += 1

def Lpop(): 
    global top 

    if top == -1: 
        print("Stack is Empty!!")
    else : 
        stack.pop(top)
        top -= 1
