# -*- coding: utf-8 -*-

# Stack implementation in python!!!

# Creating a stack.
def create_stack():
    stack = []
    return stack

# Checking stack if empty, returns True if it is.
def check_empty(stack):
    return len(stack) == 0

# Checking the length of the stack.
def check_length(stack):
    return len(stack)

# Adding items into the stack.
def push(stack, item):
    stack.append(item)
    print(item, 'was pushed into the stack!')
    
# Removing an item from the stack if it's not empty.
def pop(stack):
    if check_empty(stack):
        return "Stack is empty, nothing to remove!"
    return stack.pop()


user_input = input('Would you like to create a stack? (yes / no) > ')
while user_input != 'yes' and user_input != 'no':
    print('Please enter the correct input!')
    user_input = input('Would you like to create a stack? (yes / no) > ')

if user_input == 'yes':
     stack = create_stack()
     print('''
           Please input the number of the command you want to run:
               1. Check if the stack is empty.
               2. Check the length of the stack.
               3. Push an item into the stack.
               4. Remove the last item from the stack.
               5. Remove all items from the stack.
               6. Delete stack and quit.
               
               (Write 'quit' below to exit the program.)
           ''')


while user_input != 'no':

    command = input('Enter command: ')
    
    if command == '1':
        if check_empty(stack) == True:
            print('Stack is empty!')
        else:
            print('Stack is NOT empty.')
    
    elif command == '2':
        print('The stack has', check_length(stack), 'items.')
    
    elif command == '3':
        item = input('Enter the item you want to put inside the stack: ')
        push(stack, item)
    
    elif command == '4':
        print('The item ' + pop(stack) + ' was removed from the stack.')
    
    elif command == '5': 
        stack.clear()
        print('All items removed from stack.')
    
    elif command == '6': 
        del stack
        break
    
    elif command == 'quit':
        break
    
    else:
        print('The number you entered is NOT associated with any command.')
        
    
print('Game Over.')

