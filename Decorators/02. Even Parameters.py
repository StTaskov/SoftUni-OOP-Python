def even_parameters(function):
    def wrapper(*numbers):
        try:
            checker_for_even_numbers = [el for el in numbers if el % 2 == 0]
        except TypeError:
            return "Please use only even numbers!"

        if len(checker_for_even_numbers) == len(numbers):
            func_result = function(*tuple(checker_for_even_numbers))
            return func_result
        else:
            return "Please use only even numbers!"
    return wrapper
