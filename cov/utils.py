from typing import Set, Dict, Callable
from inspect import stack

__all__ = ["test", "mark"]


class Benchmark:
    def __init__(self, amount_of_branches: int) -> None:
        self.amount_of_branches: int = amount_of_branches
        self.reached: Set[int] = set()


results: Dict[str, Benchmark] = {}


# TODO: fix type hints
def test(amount_of_branches: int) -> Callable:
    def wrapper(function: Callable) -> Callable:
        function_name = function.__name__

        if function_name in results:
            raise ValueError()

        results[function_name] = Benchmark(amount_of_branches)

        return function

    return wrapper


def mark(branch_id: int) -> None:
    function_name = stack()[1].function

    if function_name not in results:
        raise KeyError()

    results[function_name].reached.add(branch_id)
