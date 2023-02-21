def make_bold(function):
    def wrapper(*names):
        func_result = function(*names)
        return f"<b>{func_result}</b>"

    return wrapper


def make_italic(function):
    def wrapper(*names):
        func_result = function(*names)
        return f"<i>{func_result}</i>"

    return wrapper


def make_underline(function):
    def wrapper(*names):
        func_result = function(*names)
        return f"<u>{func_result}</u>"

    return wrapper

