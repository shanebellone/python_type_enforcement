import typing


def type_enforcer(func):
    type_errors = {}

    def wrapper_func(*args):
        expected_types = typing.get_type_hints(func)
        incoming_types = args
        for type_pair in zip(incoming_types, expected_types.values()):
            incoming, expected = type_pair
            if type(incoming) != expected:
                type_errors.update({incoming: expected})
        if len(type_errors) == 0:
            func(*args)
        else:
            # Implement custom handling
            print(("Type Exception: {errors}".format(errors=type_errors)))

    return wrapper_func


@type_enforcer
def test_func(word: str, number: int):
    print(word, number)


if __name__ == '__main__':
    test_func("hello", "there")
