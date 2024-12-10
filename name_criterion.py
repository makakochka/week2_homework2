def name_criterion(name):
    if not name.strip():  # Check if name is empty or only whitespace!! ;-))
        print("User name cannot be enpty")
        return None
    elif len(name) > 20:
        print("User name should be within 20 characters")
        return None
    return name
