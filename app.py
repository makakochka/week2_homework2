from db_config import Message
from show_users import show_users
from add_user import add_user
from find_user import find_user
from delete_user import delete_user
from edit_user import edit_user


def main():
    with open("welcome.txt", "r") as file:
        content = file.read()
        print(content)

    find_users = [msg.user for msg in Message.select()]

    while True:
        command_input = input("Your command > ").upper()

        if command_input == "S":
            show_users()
        elif command_input == "A":
            add_user(find_users)
        elif command_input == "Q":
            print("Bye!")
            break
        elif command_input == "F":
            find_user(find_users)
        elif command_input == "D":
            delete_user(find_users)
        elif command_input == "E":
            edit_user(find_users)
        else:
            print(f"{command_input}: command not found")


if __name__ == "__main__":
    main()
