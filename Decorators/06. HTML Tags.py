def tags(html_tag):

    def decorator(function):

        def wrapper(*args):
            func_result = function(*args)
            return f"<{html_tag}>{func_result}</{html_tag}>"
        return wrapper
    return decorator
