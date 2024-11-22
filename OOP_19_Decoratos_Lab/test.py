def upper(function) -> object:
    def wrapper(message):
        result = function(message)
        return result.upper()
    return wrapper


@upper
def print_message(message):
    return message


print(print_message("Text-One"))
print(print_message("Text-Two"))
print(print_message("Text-Three"))
print(print_message("Text-Four"))
print(print_message("Text-Five"))
