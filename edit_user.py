from db_config import Message
from name_criterion import name_criterion
from age_criterion import age_criterion


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
                        print(f"Update user: {new_user_name}")
                except ValueError:
                    print("Please enter a valid number for the age.")
                break
    else:
        print(f"Sorry, {entered_name} is invalid")
