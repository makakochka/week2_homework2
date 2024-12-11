def name_criterion(name):
    if not name.strip():  # Check if name is empty or only whitespace!! ;-))
        print("User name can't be blank")
        return None
    elif len(name) > 20:
        print("User name is too long(maximun is 20 characters)")
        return None
    return name
