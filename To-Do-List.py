tasks=[]

def add_task():
    "Adding tasks into to-do-list"
    task=input("Enter a new task:")
    tasks.append(task)
    print("Task added successfully")

def view_tasks():
    if len(tasks)==0:
        print("no tasks")
    else:
        print('List of tasks:')
        for i,task in enumerate(tasks):
            print(f"{i+1}. {task}")

def delete_tasks():
    if len(tasks)==0:
        print('no tasks to delete.')
    else:
        for i,task in enumerate(tasks):
            print(f"{i+1}. {task}")

        choice=int(input('Enter the task number to delete:'))
        if 0<choice<=len(tasks):
            del tasks[choice-1]
            print('Task deleted successfully.')
        else:
            print('Invalid task number.')



def main():
    while True:
        print('\n==== To-do-list operation ====')
        print('1.Add Task')
        print('2.View Tasks')
        print('3.Delete task')
        print('4.Quit')

        choice=int(input("Enter your choice: "))
        if choice==1:
            add_task()
        elif choice==2:
            view_tasks()
        elif choice==3:
            delete_tasks()
        elif choice==4:
            print("Thank you for using the To-Do-Application.")
        else:
            print('Invalid choice.Please try again.')



if __name__=="__main__":
    main()

