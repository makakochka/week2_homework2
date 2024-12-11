from db_config import Message
from name_criterion import name_criterion
from age_criterion import age_criterion


def add_user(find_users):
    new_user_name = name_criterion(input("New user name > "))
    if new_user_name is None:  # Check if name validation failed!! ;-)
        return
    if new_user_name in find_users:
        new_age_input = input("New user age > ")
        print(f"Duplicated user name {new_user_name}")
    else:
        try:
            new_age_input = input("New user age > ")
            new_age = int(new_age_input)
            new_age = age_criterion(new_age)
            if new_age is not None:
                Message.create(user=new_user_name, age=new_age, content="None")
                find_users.append(new_user_name)
        except ValueError:
            print("Please enter a valid number for the age.")
