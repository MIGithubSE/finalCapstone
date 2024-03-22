# Capstone Project 2

from datetime import datetime
import os

# The logic to check if the task is overdue.
def is_overdue(due_date):
    """
    Check if a task is overdue based on its due date.
    Assuming the due date is in 'YYYY-MM-DD' format.
    """
    due_date_format = "%Y-%m-%d"
    due_date_obj = datetime.strptime(due_date, due_date_format)
    current_date_obj = datetime.now()
    return current_date_obj > due_date_obj   

def login():
    """
    Prompts for a username and password and verifies them against user.txt.
    """
    ensure_user_file()  # Make sure the user.txt file exists

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        with open("user.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",", 1)
                if username == stored_username and password == stored_password:
                    print("Login successful!")
                    return True  # or any other indicator of a successful login
            # If no match was found during the loop, indicate failure
            print("Invalid username or password. Please try again.")
            return False
    except FileNotFoundError:
        print("User file not found. Please make sure the user file exists.")
        return False
    except IOError as e:
        print(f"An error occurred accessing the user file: {e}")
        return False

def ensure_user_file():
    """
    Ensures that the user.txt file exists. If not, creates it.
    """
    try:
        with open("user.txt", "a+"):  # Open in append mode with read/write permissions
            pass  # File exists or created successfully
    except IOError as e:
        print(f"An error occurred while accessing or creating the user file: {e}")

def reg_user():
    """
    Register a new user by prompting for username and password,
    and writing the information to the user.txt file.
    """
    ensure_user_file()  # Ensure user.txt exists

    # Prompt the user to enter a new username and password
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    try:
        with open("user.txt", "r") as file:
            existing_users = [line.split(",")[0].strip() for line in file]
    except FileNotFoundError:
        # No need to handle here; ensure_user_file already creates the file
        pass

    if username in existing_users:
        print("Username already exists. Please try a different username.")
    else:
        try:
            with open("user.txt", "a") as file:
                file.write(f"{username},{password}\n")  # Write both username and password
            print("User registered successfully.")
        except Exception as e:
            print(f"An error occurred while registering user: {e}")

# Define function to add a task (a)
def add_task():
    # Prompt the user to input details of the task
    task = input("Enter task: ")
    user = input("Assign task to user: ")
    due_date = input("Enter due date (yyyy-mm-dd): ")

    # Set the initial status of the task to "No" (not completed)
    status = "No"

    # Open the tasks.txt file in append mode and write the task details to it
    try:
        with open("tasks.txt", "a") as file:
            file.write(f"{task},{user},{due_date},{status}\n")

        # Print a message indicating successful addition of the task    
        print("Task added successfully.")
    except Exception as e:
        print(f"An error occurred while adding task: {e}")

# Define function to view all tasks (VM)
def view_all():
    """
    This function reads tasks from the 'tasks.txt' file and prints them out.
    Each task's details are displayed in an easy-to-read format.
    """
    try:
        # Attempt to open the tasks.txt file in read mode.
        with open("tasks.txt", "r") as file:
            """
            Read each line in the file, strip trailing whitespace,
            split each line by commas into a list of task details,
            and compile all tasks into a list of lists.
            """
            tasks = [line.strip().split(",") for line in file]

        """
        Loop through the list of tasks, using enumerate to get both
        the index (for task numbering) and the task details.
        """   
        for index, task in enumerate(tasks, start=1):
            # Print out each task's details in a formatted string for clarity,
            print(f"{index}. Task: {task[0]}, Assigned to: {task[1]}, Due Date: {task[2]}, Status: {task[3]}")
    except FileNotFoundError:
        #If tasks.txt does not exist, inform the user that the tasks file could not be found
        print("Tasks file not found.")

# Define function to view tasks assigned to the current user
def view_mine():
    """
    This function allows users to view and potentially edit tasks assigned to them.
    Users input their username to retrieve tasks assigned to them from the 'tasks.txt' file.
    They can mark tasks as complete or edit task details such as the username and due date.
    """
    try:
        username = input("Enter your username: ")
        # Attempt to open the 'tasks.txt' file in read mode.
        with open("tasks.txt", "r") as file:
            tasks = [line.strip().split(",") for line in file if line.strip().split(",")[1] == username]
    except FileNotFoundError:
        # Handle the case where the 'tasks.txt' file does not exist.
        print("Tasks file not found.")
        return
    except Exception as e:
        # Handle other unexpected errors that might occur during file processing.
        print(f"An error occurred: {str(e)}")
        return
    
    # Display tasks assigned to the user along with their details.
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. Task: {task[0]}, Due Date: {task[2]}, Status: {task[3]}")

    # Prompt the user to choose a task to edit or mark as complete.
    task_choice = input("Enter the number of the task you want to edit/mark as complete (-1 to return to the main menu): ")
    if task_choice == "-1":
        return
    else:
        try:
            # Convert the user's input into an integer to select the task index.
            task_index = int(task_choice) - 1

            # Check if the selected task index is within the range of available tasks.
            if 0 <= task_index < len(tasks):
                # Check if the task is already completed.
                if tasks[task_index][3] == "Yes":
                    print("This task is already completed and cannot be edited.")
                    return

                # Prompt the user to choose an action: complete or edit.
                action = input("Do you want to mark the task as complete (enter 'complete') or edit the task (enter 'edit')? ")

                # Update the task status to 'Yes' to mark it as complete.
                if action == "complete":
                    tasks[task_index][3] = "Yes"
                    print("Task marked as complete successfully.")

                elif action == "edit":
                    # Prompt the user to enter new details for the task (username and due date).
                    new_username = input("Enter new username: ")
                    new_due_date = input("Enter new due date: ")

                    # Update the task details with the new information provided by the user.
                    tasks[task_index][1] = new_username
                    tasks[task_index][2] = new_due_date
                    print("Task updated successfully.")
                else:
                    print("Invalid action. Please enter 'complete' or 'edit'.")
            else:
                print("Invalid task number.")

        except ValueError:
            # Handle the case where the user enters an invalid task number.
            print("Invalid input. Please enter a valid task number.")

    try:
        # Attempt to open the 'tasks.txt' file in write mode to update task details.
        with open("tasks.txt", "w") as file:
            # Write the updated task details back to the file.
            for task in tasks:
                file.write(",".join(task) + "\n")

    except Exception as e:
        # Handle errors that might occur while writing to the file.
        print(f"An error occurred while writing to the file: {str(e)}")

# Define function to generate reports (GR)
def generate_reports():
    """
    This function generates reports based on the tasks and user data stored in files.
    It calculates various statistics such as completed tasks, uncompleted tasks, and overdue tasks.
    The reports are written to separate text files for task overview and user overview.
    """
    try:
        # Read task data from the 'tasks.txt' file and split each line into task details.
        with open("tasks.txt", "r") as file:
            tasks = [line.strip().split(",") for line in file]
    except FileNotFoundError:
        print("Tasks file not found. No tasks to report on.")
        return
    except IOError as e:
        print(f"An error occurred accessing the tasks file: {e}")
        return

    # Calculate total tasks and handle cases where no tasks are found.
    total_tasks = len(tasks)
    if total_tasks == 0:
        print("No tasks found. Cannot generate reports.")
        return

    # Count completed, uncompleted, and overdue tasks.
    completed_tasks = sum(1 for task in tasks if task[3] == "Yes")
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for task in tasks if task[3] == "No" and is_overdue(task[2]))

    # Calculate percentages of incomplete and overdue tasks.
    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100 if total_tasks else 0
    overdue_percentage = (overdue_tasks / total_tasks) * 100 if total_tasks else 0

    try:
        # Write task overview report to 'task_overview.txt' file.
        with open("task_overview.txt", "w") as file:
            file.writelines([
                f"Total tasks: {total_tasks}\n",
                f"Completed tasks: {completed_tasks}\n",
                f"Uncompleted tasks: {uncompleted_tasks}\n",
                f"Overdue tasks: {overdue_tasks}\n",
                f"Percentage of tasks that are incomplete: {incomplete_percentage:.2f}%\n",
                f"Percentage of tasks that are overdue: {overdue_percentage:.2f}%\n",
            ])
    except IOError as e:
        print(f"An error occurred writing to the task overview report: {e}")
        return

    try:
        # Read user data from the 'user.txt' file.
        with open("user.txt", "r") as file:
            users = [line.strip().split(",")[0] for line in file]
    except FileNotFoundError:
        print("User file not found. Cannot generate user reports.")
        return
    except IOError as e:
        print(f"An error occurred accessing the user file: {e}")
        return

    # Calculate total users and tasks assigned to each user.
    total_users = len(users)
    tasks_per_user = {user: sum(1 for task in tasks if task[1] == user) for user in users}

    try:
        # Write user overview report to 'user_overview.txt' file.
        with open("user_overview.txt", "w") as file:
            file.write(f"Total users: {total_users}\n")
            file.write(f"Total tasks generated: {total_tasks}\n")
            for user in users:
                user_tasks = tasks_per_user.get(user, 0)
                completed_user_tasks = sum(1 for task in tasks if task[1] == user and task[3] == "Yes")
                overdue_user_tasks = sum(1 for task in tasks if task[1] == user and task[3] == "No" and is_overdue(task[2]))
                completed_percentage = (completed_user_tasks / user_tasks) * 100 if user_tasks else 0
                overdue_percentage = (overdue_user_tasks / user_tasks) * 100 if user_tasks else 0

                file.writelines([
                    f"\nUser: {user}\n",
                    f"Total tasks assigned: {user_tasks}\n",
                    f"Percentage of total tasks assigned: {(user_tasks / total_tasks * 100) if total_tasks else 0:.2f}%\n",
                    f"Percentage of completed tasks: {completed_percentage:.2f}%\n",
                    f"Percentage of overdue tasks: {overdue_percentage:.2f}%\n",
                ])
    except IOError as e:
        print(f"An error occurred writing to the user overview report: {e}")

    print("Reports generated successfully.")

# Define function to display statistics    
def display_statistics():
    """
    This function displays the task and user overview reports.
    If the reports are not found, it triggers their generation.
    """

    # Attempt to open and read the task overview report.
    try:
        # Open the 'task_overview.txt' file in read mode.
        with open("task_overview.txt", "r") as task_file:
            # Print the title and contents of the task overview report.
            print("Task Overview Report:")
            print(task_file.read())

    # Handle the case where the task overview report file does not exist.        
    except FileNotFoundError:
        # Inform the user that the task overview report is missing and will be generated.
        print("Task overview report not generated. Generating now...")
        generate_reports()  # Generate the task overview report

    # Repeat the process for the user overview report.
    try:
        # Open the 'user_overview.txt' file in read mode.
        with open("user_overview.txt", "r") as user_file:
            # Print the title and contents of the user overview report.
            print("User Overview Report:")
            print(user_file.read())

    # Handle the case where the user overview report file does not exist.        
    except FileNotFoundError:
        # Inform the user that the user overview report is missing and will be generated.
        print("User overview report not generated. Generating now...")
        generate_reports()  # Generate the user overview report
                                 
def login_user():
    try:
        username = input("Enter your username: ")  # This takes username from the user as an input
        password = input("Enter your password: ")  # This takes the password from the user as an input

        with open("user.txt", "r") as file:  # Path to credentials
            users = [line.strip().split(",") for line in file]

        for user in users:
            if user[0] == username and user[1] == password:  # Check if the username and password match
                print("Login successful!")
                return True

        # This line is printed if either of the credentials didn't match
        print("Invalid username or password. Please try again.")
        return False
    except FileNotFoundError:
        print("User file not found. Please make sure the user file exists.")
        return False
    except IOError as e:
        print(f"An error occurred accessing the user file: {e}")
        return False
    
def main():
    print("Welcome to the Task Manager!")
    if login_user():  # Assuming login_user() prompts for username/password and returns True if successful
        print("Login successful. Welcome to the Task Manager.")

        while True:
            print("\nPlease select one of the following options:")
            print("r - register user")
            print("a - add task")
            print("va - view all tasks")
            print("vm - view my tasks")
            print("gr - generate reports")
            print("ds - display statistics")
            print("e - exit")
            option = input("Enter your choice: ").lower()

            if option == "r":
                reg_user()
            elif option == "a":
                add_task()
            elif option == "va":
                view_all()
            elif option == "vm":
                view_mine()
            elif option == "gr":
                generate_reports()
            elif option == "ds":
                # Assuming a function display_statistics() that reads the reports and displays stats
                display_statistics()
            elif option == "e":
                print("Thank you for using the Task Manager. Goodbye!")
                break  # Exit the loop and end the program
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    main()