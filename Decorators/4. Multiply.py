def multiply(times):

    def decorator(function):
        def wrapper(number):
            function_result = function(number)
            return function_result * times
        return wrapper

    return decorator