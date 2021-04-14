SOME_VAR = 42


class SomeError(Exception):
    pass


def func():
    raise SomeError("Something went wrong...")


func()
