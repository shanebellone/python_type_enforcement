import typing


def enforce_type(func):
    def wrapper_func(*args):
        # Get type hints from decorated func
        expected_types = typing.get_type_hints(func)
        # Build dictionary with comprehension with if evaluation
        type_errors = {arg: expected for arg, expected in zip(args, expected_types.values()) if type(arg) != expected}
        # Check for errors
        if len(type_errors) == 0:
            # If types match, return decorated function
            func(*args)
        else:
            # Otherwise, raise TypeError
            error = "\tCheck {func}{args}: \t{errors}".format(func=func.__name__, args=args, errors=type_errors)
            raise TypeError(error)

    return wrapper_func


@enforce_type
def test_func(word: str, number: int):
    print(word, number)


if __name__ == '__main__':
    test_func("hello", "there")
