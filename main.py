import time

from domain.User import User
from infrastructure.JsonUserRepository import JsonUserRepository
from validators.UserValidators import UserValidators

LIST_OR_OPERATIONS = ["Create User", "View User", "Update User", "Delete User", "Show All Users", "Exit"]
repository = JsonUserRepository("data/data.json")


def main():
    while True:
        display_menu()
        operation = ask_input("Enter the operation number: ")

        try:
            operation_number = int(operation)
            if 0 <= operation_number < len(LIST_OR_OPERATIONS):
                if operation_number == 0:
                    print("Exiting...")
                    time.sleep(1)
                    break
                execute_operation(operation_number-1)
            else:
                print("Invalid operation number.\n")
        except ValueError:
            print("Invalid input format.\n")


def execute_operation(operation: int):
    if LIST_OR_OPERATIONS[operation] == "Create User":
        data = collect_user_data()
        user = User(data)
        repository.create_user(user)
        print("User created successfully.\n")

    elif LIST_OR_OPERATIONS[operation] == "View User":
        user_id = ask_input("Enter user ID: ")
        user = repository.get_user(user_id)
        if user:
            print(user.to_dict())
        else:
            print("User not found.\n")

    elif LIST_OR_OPERATIONS[operation] == "Update User":
        user_id = ask_input("Enter user ID to update: ")
        if repository.get_user(user_id) is not None:
            updated_data = collect_user_data()
            success = repository.update_user(user_id, updated_data)
            print("User updated successfully.\n" if success else "Could not update User.\n")
        else:
            print("User not found.\n")

    elif LIST_OR_OPERATIONS[operation] == "Delete User":
        user_id = ask_input("Enter user ID to delete: ")
        success = repository.delete_user(user_id)
        print("User deleted.\n" if success else "User not found.\n")

    elif LIST_OR_OPERATIONS[operation] == "Show All Users":
        users = repository.get_all_users()
        if users:
            for user in users:
                print(user.to_dict())
        else:
            print("No users found.\n")


def collect_user_data():
    # username = input("Username: ")
    # email = input("Email: ")
    # name = input("Full name: ")
    # phone = input("Phone number: ")
    # age = input("Age: ")
    username =ask_and_validate_input("Username", lambda value: value and len(value) > 0 and repository.get_user_by_username(value) is None, "Username must be non-empty and unique.")
    email = ask_and_validate_input("Email", UserValidators.validate_email)
    name = ask_and_validate_input("Fullname", UserValidators.validate_name)
    phone = ask_and_validate_input("Phone", UserValidators.validate_phone)
    age = ask_and_validate_input("Age", UserValidators.validate_age)


    return {
        "username": username,
        "email": email,
        "name": name,
        "phone": phone,
        "age": int(age)
    }

def ask_and_validate_input(field_name: str, validator, message=None):
    while True:
        input_value = input(f"{field_name}: ")
        if input_value and validator(input_value):
            return input_value
        print(f"Invalid input for {field_name}. Please enter a valid {field_name}." if message is None else message)


def display_menu():
    print("\n=== CRUD Repository Menu ===")
    count = 0
    for op in LIST_OR_OPERATIONS:
        count += 1
        print(f"{count if count < len(LIST_OR_OPERATIONS) else 0}. {op}")

def ask_input(prompt):
    return input(prompt)

def return_to_menu(message = ""):
    print(message)
    main()


if __name__ == "__main__":
    print("The program CRUD Repository is launching...")
    # time.sleep(2)
    input("Press 'ENTER' to start")
    main()