from db_config import Message
from name_criterion import name_criterion


def find_user(find_users):
    entered_name = name_criterion(input("User name > "))
    if entered_name in find_users:
        for msg in Message.select():
            if msg.user == entered_name:
                print(f"Name: {msg.user}, Age: {msg.age}")
                break
    else:
        print(f"Sorry, {entered_name} is not found")
