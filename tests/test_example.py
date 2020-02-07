from example import Foo


def test_foo():
    foo = Foo()
    assert str(foo) == 'foo'
