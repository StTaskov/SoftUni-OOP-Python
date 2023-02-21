def type_check(type):

    def decorator(function):

        def wrapper(num):

            if not isinstance(num, type):
                return "Bad Type"
            else:
                result = function(num)
                return result

        return wrapper

    return decorator
