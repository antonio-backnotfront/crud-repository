import time

def main():
    display_menu()
    operationNumber = ask_input("Enter the operation number (e.g 1): ")
    try:
        operation  = int(operationNumber)
        if operation > 0 and operation < 6:
            print("Executing")
        else:
            return_to_menu("Invalid operation number")
    except ValueError:
        return_to_menu("Invalid operation format.")










def display_menu():
    print("=== User CRUD Repository Menu ===")
    print("1. Create User")
    print("2. View User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Show All Users")
    print("6. Exit")

def ask_input(prompt):
    return input(prompt);

def return_to_menu(message = ""):
    print(message)
    main()


if __name__ == "__main__":
    print("The program User CRUD Repository is launching...")
    time.sleep(2)
    input("Press 'ENTER' to start")
    main()