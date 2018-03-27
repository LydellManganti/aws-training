def isNumberValid(number):
    if number is None or number == '':
        return False
    if int(number) < 1:
        return False
    return True

def isNameValid(name):
    if name is None or name == '':
        return False
    return True
