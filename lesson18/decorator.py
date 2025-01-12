def input_error(func):
    def wrapper(contacts, *args):
        try:
            result = func(contacts, *args)
        except ValueError:
            result = 'Error! Phone number is incorrect'
        return result
    return wrapper

