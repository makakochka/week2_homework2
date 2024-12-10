from db_config import Message
from find_user import find_user
from delete_user import delete_user
from edit_user import edit_user
from name_criterion import name_criterion
from age_criterion import age_criterion


def show_users():
    for msg in Message.select():
        print(f"{msg.user}, {msg.age}")


def add_user(find_users):
    new_user_name = name_criterion(input("New user name > "))
    if new_user_name in find_users:
        print(f"Duplicated user name {new_user_name}")
    else:
        try:
            new_age_input = input("New user age > ")
            new_age = int(new_age_input)  # Convert the input to an integer
            new_age = age_criterion(new_age)
            if new_age is not None:
                Message.create(user=new_user_name, age=new_age, content="None")
                find_users.append(new_user_name)
        except ValueError:
            print("Please enter a valid number for the age.")


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
