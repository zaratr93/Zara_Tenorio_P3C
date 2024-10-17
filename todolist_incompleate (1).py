# A simple to-do list manager for high school students using functions and list comprehension

# Initial to-do list
todo_list = ["Math homework", "Science project", "Read history book", "Practice piano"]

# Function to display the current to-do list
def display_todo_list():
    #TODO display the list
    print(f"ToDo list:\n")
    for i in todo_list:
        print (i)


# Function to add a new task
def add_task():
    #TODO the user wants to add a task. 
    task = input("task: ")
    todo_list.append(task)
display_todo_list()


# Function to remove a task by its name
def remove_task():
    #TODO 
    task = input("Write the name of the task you wantto remove: ")
    if task in todo_list:
        todo_list.remove(task)
        display_todo_list()
    else: 
        print("there is an ERROR")
        display_todo_list()

# Function to find the index of a task
def find_task():
    print("What task would you like to find?: ")
    task = input()
    index_task = todo_list.index
    #The user wants to know in what position is a task. 
    if task in todo_list:
        print(index_task(task))
        
    else: 
        print("ERROR")
 
    display_todo_list()
# Function to complete and remove the first task
def complete_task():
    #The user wants to remove the first task. 
    del todo_list[0]
    print("you completed this task")
    display_todo_list()


# Function to filter tasks containing a specific keyword using list comprehension
def filter_tasks():
    #TODO create a list comprehension variable to filter tasks containing a specific keyword
    keyword = input("write a keyword of the task: ")
    filtered_tasks = [task for task in todo_list if keyword in task]
    print(f"\nTasks containing '{keyword}':")
    print(filtered_tasks if filtered_tasks else "No tasks found.")
    


# Main program

# Main menu to choose options
def main():
    while True:
        print("\nTo-Do List Manager Menu")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Find Task")
        print("5. Complete First Task")
        print("6. Filter Tasks by Keyword")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")

        #TODO create the if staments for the user. 

        if choice == "1": 
            display_todo_list()
            
        if choice == "2": 
           add_task()
             
        if choice == "3": 
            remove_task()
            
        if choice == "4": 
            find_task()
            
        if choice == "5":
            complete_task()
            
        if choice == "6":
            filter_tasks()
        if choice == "7":
            break
            
        

# Run the main function
main()

