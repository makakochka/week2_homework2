from db_config import Message


def show_users():
    for msg in Message.select():
        print(f"{msg.user}, {msg.age}")
