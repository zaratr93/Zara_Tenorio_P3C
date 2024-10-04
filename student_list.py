students = ["Seraphina","Alaric","Isolde","Thaddeus","Evangeline","Octavius","Lavinia","Aurelius","Genevieve","Percival"]
def display_students():
    print(f"Current students:\n")
    for i in students:
        print (i)
    
    
    print(f"") 


def add_student():
   name = input("name: ")
   students.append(name)
display_students()

def remove_student():
    name = input("Write the name of the student you wantto remove: ")
    if name in students:
        students.remove(name)
    else: 
        print("there is an ERROR")
        
    display_students()
 
def pop_student():
    if len(students) == 0:
        print("There are no stuudents left")
    else:
        print(students[-1])
        students.pop()
    display_students()

def update_student():
    
    name_update = input("name: ")
   
    if name_update in students:
        index = students.index(name_update)
        new_name = input("new name: ")
        
        students[index] = new_name
    
    else: 
        print("No student")
    display_students()
# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1": 
            add_student()
            
       
        if choice == "2": 
           remove_student()
             
        if choice == "3": 
            pop_student()
            
        if choice == "4": 
            update_student()
        

# Start the program
menu()
display_students()