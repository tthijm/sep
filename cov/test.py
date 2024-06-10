from utils import test, mark, results


@test(2)
def absolute(x: int) -> int:
    if x < 0:
        mark(0)
        return -x
    else:
        mark(1)
        return x


def test_one():
    assert absolute(10) == 10
    assert absolute(0) == 0
    assert absolute(-10) == 10


test_one()
print(results)
