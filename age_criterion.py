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
