from db_config import Message


def show_users():
    for msg in Message.select():
        print(f"Name: {msg.user}, Age: {msg.age}")
