from microsetta_private_api.util.decorator_util import build_param_map, \
    bind_param_map


def my_test_decorator(func):
    pmap = build_param_map(func, ['x', 'y', 'z', 'override'])

    def wrapper(*args, **kwargs):
        bound_params = bind_param_map(pmap,
                                      {'override': "Fig Newton"},
                                      args,
                                      kwargs)
        return bound_params.get('x'), \
            bound_params.get('y'), \
            bound_params.get('z'), \
            bound_params.get('override')

    return wrapper


def test_1():
    @my_test_decorator
    def func1(z, a, b, x=7, d=4, y=None):
        assert False

    assert func1("z", "a", "b", "x", "d", "y") == ("x", "y", "z", "Fig Newton")
    assert func1("zz2", "a", "b", d=27, y="foobar") == \
        (7, "foobar", "zz2", "Fig Newton")

    # Hah, you'd think this wouldn't compile, and it would throw a TypeError
    # if the wrapper method ever called into func1, but the wrapper itself
    # has no idea what the args and kwargs are, and doesn't care if they
    # overlap.  Bound params happens to prefer args over kwargs arbitrarily.
    assert func1("z", "a", "b", "x", x=15) == ("x", None, "z", "Fig Newton")


def test_2():
    @my_test_decorator
    def func2(x=29):
        assert False

    assert func2(15) == (15, None, None, "Fig Newton")
    assert func2(y="Can'tSeeThis") == (29, None, None, "Fig Newton")
    assert func2(override="OrThis") == (29, None, None, "Fig Newton")


def test_3():
    @my_test_decorator
    def func3(override):
        assert False

    assert func3("Nope") == (None, None, None, "Fig Newton")
