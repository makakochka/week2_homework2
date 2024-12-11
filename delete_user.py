from db_config import Message
from name_criterion import name_criterion


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
