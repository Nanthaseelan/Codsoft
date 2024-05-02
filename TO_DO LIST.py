#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def display_list(todo_list):
    print("To-Do List:")
    for index, item in enumerate(todo_list, start=1):
        print(f"{index}. {item}")


def add_task(todo_list, task):
    todo_list.append(task)
    print(f"'{task}' added to the To-Do list.")


def remove_task(todo_list, task_index):
    if task_index >= 1 and task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"'{removed_task}' removed from the To-Do list.")
    else:
        print("Invalid task index.")


def main():
    todo_list = [1,2,3,4,5]

    while True:
        print("\n1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_list(todo_list)
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
        elif choice == '3':
            task_index = int(input("Enter the index of the task to remove: "))
            remove_task(todo_list, task_index)
        elif choice == '4':
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


# In[ ]:




