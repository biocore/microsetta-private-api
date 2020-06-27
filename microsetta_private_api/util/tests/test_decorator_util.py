from microsetta_private_api.util.decorator_util import \
    has_non_keyword_arguments


def test_non_keyword_args():
    def func1(x, y, z):
        pass

    def func2(x=1, y=2, z=3):
        pass

    def func3(*, x=1, y=2, z=3):
        pass

    def func4(a, b, c, *, x=1, y=2, z=3):
        pass

    assert has_non_keyword_arguments(func1)
    assert has_non_keyword_arguments(func2)
    assert not has_non_keyword_arguments(func3)
    assert has_non_keyword_arguments(func4)
