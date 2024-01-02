#!/usr/bin/python3
"""This module is to export a csv file of the PAI data
"""
import requests
import sys
import csv


def get_employee_todo_progress(employee_id):
    """Define the API endpoint URL for TODOs"""
    todos_url = f"https: //jsonplaceholder.typicode.com/todos?"\
        f"userId={employee_id}"

    todos_response = requests.get(todos_url)

    if todos_response.status_code == 200:
        todos = todos_response.json()

        user_url = f"https://jsonplaceholder.typicode.com/users/"\
        f"{employee_id}"
        user_response = requests.get(user_url)

        if user_response.status_code == 200:
            user_data = user_response.json()
            employee_name = user_data['name']

            filename = f"{employee_id}.csv"
            with open(filename, mode='w', newline='') as csv_file:
                fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                              "TASK_TITLE"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()

                for todo in todos:
                    writer.writerow({
                        "USER_ID": employee_id,
                        "USERNAME": employee_name,
                        "TASK_COMPLETED_STATUS": "Completed" if
                        todo['completed'] else "Not Completed",
                        "TASK_TITLE": todo['title']
                    })

                """print(f"CSV file '{filename}' has been
                created successfully.")"""
        else:
            print(f"Error: Unable to fetch user information for employee ID {employee_id}")
    else:
        print(f"Error: Unable to fetch TODO list for employee ID"
              f"{employee_id}")


if __name__ == "__main__":
    """Check if an employee ID is provided as a command-line argument"""
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])

        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
