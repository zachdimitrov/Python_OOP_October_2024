from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper():
        result = function()
        return [el for el in result if el.lower() in "aoeiyu"]
    return wrapper


@vowel_filter
def get_letters():
    """My Function Doc"""
    return["A", "b", "c", "d", "e"]


print(get_letters())
print(get_letters.__doc__)