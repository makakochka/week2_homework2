from db_config import Message


def name_criterion(name):
    if len(name) > 20:
        print("User name should be within 20 characters")
        return name
    return name


def is_real_number(x):
    return isinstance(x, (int, float))


def age_criterion(age):
    if is_real_number(age):
        if age < 0:
            print("Age is a negative number")
            return None
        elif (age - age // 1 != 0) and (0 < age <= 120):
            print("Age is not a positive integer")
            return None
        elif 120 < age:
            print("Age is grater than 120")
            return None
        else:
            return age
    else:
        print("That's not a real number")
        return None


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


def find_user(find_users):
    entered_name = name_criterion(input("User name > "))
    if entered_name in find_users:
        for msg in Message.select():
            if msg.user == entered_name:
                print(f"Name: {msg.user}, Age: {msg.age}")
                break
    else:
        print(f"Sorry, {entered_name} is not found")


def delete_user(find_users):
    entered_name = name_criterion(input("User name > "))
    if entered_name in find_users:
        for msg in Message.select():
            if msg.user == entered_name:
                msg.delete_instance()
                find_users.remove(msg.user)
                print(f"User {entered_name} is deleted")
                break
    else:
        print(f"Sorry, {entered_name} is not found")


def edit_user(find_users):
    entered_name = name_criterion(input("User name > "))
    if entered_name in find_users:
        for msg in Message.select():
            if msg.user == entered_name:
                try:
                    new_user_name = input("New user name > ")
                    msg.user = new_user_name
                    new_age_input = input(f"New user age({msg.age}) > ")
                    new_age = int(new_age_input)  # Convert the input to an integer
                    new_age = age_criterion(new_age)
                    if new_age is not None:
                        msg.age = new_age
                        msg.save()
                        print(
                            f"{entered_name} whose age was {msg.age} has been updated to {new_user_name} whose age is {new_age}"
                        )
                except ValueError:
                    print("Please enter a valid number for the age.")
                break
    else:
        print(f"Sorry, {entered_name} is invalid")


def main():
    print("===== Welcome to CRM Application=====")
    print("[S]how: Show all users info")
    print("[A]dd: Add new user")
    print("[Q]uit: Quit The Application")
    print("[F]ind: Find existing user")
    print("[E]dit: Edit existing user")
    print("[D]elete: Delete existing user")
    print("======================================")

    find_users = [msg.user for msg in Message.select()]

    while True:
        command_input = input("Your command > ").upper()

        if command_input == "S":
            show_users()
        elif command_input == "A":
            add_user(find_users)
        elif command_input == "Q":
            print("Exiting the application. Goodbye!")
            break
        elif command_input == "F":
            find_user(find_users)
        elif command_input == "D":
            delete_user(find_users)
        elif command_input == "E":
            edit_user(find_users)
        else:
            print("That command is invalid")


if __name__ == "__main__":
    main()
