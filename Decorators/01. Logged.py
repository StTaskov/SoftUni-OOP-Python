def logged(function):

    def wrapper(*args):
        function_result = function(*args)
        return f"you called {function.__name__}{args}\nit returned {function_result}"

    return wrapper
