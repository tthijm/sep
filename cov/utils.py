from typing import Dict, Callable
from cov.benchmark import Benchmark
import inspect

__all__ = ["test", "mark"]

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
    function_name = inspect.stack()[1].function
    benchmark = results.get(function_name)

    if benchmark is None or benchmark.is_valid(branch_id) is False:
        raise KeyError()

    benchmark.mark(branch_id)


def print_results() -> None:
    print(results)
