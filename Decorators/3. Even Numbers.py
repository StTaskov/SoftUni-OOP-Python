def even_numbers(function):

    def wrapper(numbers):
        function_result = function(numbers)
        return [number for number in function_result if number % 2 == 0]

    return wrapper
