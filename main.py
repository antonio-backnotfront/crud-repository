import time

LIST_OR_OPERATIONS = ["Create User", "View User", "Update User", "Delete User", "Show All Users", "Exit"]

def main():
    display_menu()
    operationNumber = ask_input("Enter the operation number: ")
    try:
        operation  = int(operationNumber)
        if 0 < operation < 6:
            print("Executing")
        else:
            return_to_menu("Invalid operation number")
    except ValueError:
        return_to_menu("Invalid operation format.")





def display_menu():
    print("=== CRUD Repository Menu ===")
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
    time.sleep(2)
    input("Press 'ENTER' to start")
    main()