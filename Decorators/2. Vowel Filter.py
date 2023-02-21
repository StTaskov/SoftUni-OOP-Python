def vowel_filter(function):

    def wrapper():
        function_result = function()
        result = [letter for letter in function_result if letter.lower() in "aouei"]
        return result

    return wrapper