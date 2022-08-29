import typing


def enforce_type(func):
    def wrapper_func(*args):
        expected_types = typing.get_type_hints(func)
        type_errors = {arg: expected for arg, expected in zip(args, expected_types.values()) if type(arg) != expected}
        if len(type_errors) == 0:
            func(*args)
        else:
            error = "\tCheck {func}{args}: \t{errors}".format(func=func.__name__, args=args, errors=type_errors)
            raise TypeError(error)

    return wrapper_func


@enforce_type
def test_func(word: str, number: int):
    print(word, number)


if __name__ == '__main__':
    test_func("hello", "there")
