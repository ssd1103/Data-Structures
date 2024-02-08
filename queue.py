# -*- coding: utf-8 -*-

# Queue implementation in python!!!

# Creating a queue.
def create_queue():
    queue = []
    return queue

# Checking stack if empty, returns True if it is.
def check_empty(queue):
    return len(queue) == 0

# Checking the length of the queue.
def check_length(queue):
    return len(queue)

# Adding an item into the queue.
def enqueue(queue, item):
    queue.append(item)
    print(item, 'was added into the queue!')

# Removing an item from the queue.
def dequeue(queue):
    if check_empty(queue):
        return "Queue is empty, nothing to remove!"
    return 'The item ' + queue.pop(0) + ' was removed from the queue.'

user_input = input('Would you like to create a queue? (yes / no) > ')
while user_input != 'yes' and user_input != 'no':
    print('Please enter the correct input!')
    user_input = input('Would you like to create a queue? (yes / no) > ')

if user_input == 'yes':
     queue = create_queue()
     print('''
           Please input the number of the command you want to run:
               1. Check if the queue is empty.
               2. Check the length of the queue.
               3. Add an item into the queue.
               4. Remove the first item from the queue.
               5. Remove all items from the queue.
               6. Delete queue and quit.
               
               (Write 'quit' below to exit the program.)
           ''')


while user_input != 'no':

    command = input('Enter command: ')
    
    if command == '1':
        if check_empty(queue) == True:
            print('Queue is empty!')
        else:
            print('Queue is NOT empty.')
    
    elif command == '2':
        print('The queue has', check_length(queue), 'items.')
    
    elif command == '3':
        item = input('Enter the item you want to put inside the queue: ')
        enqueue(queue, item)
    
    elif command == '4':
        print(dequeue(queue))
    
    elif command == '5': 
        queue.clear()
        print('All items removed from queue.')
    
    elif command == '6': 
        del queue
        break
    
    elif command == 'quit':
        break
    
    else:
        print('The number you entered is NOT associated with any command.')
        
    
print('Game Over.')