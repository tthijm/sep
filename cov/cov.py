from typing import List, Dict, Callable
from tabulate import tabulate
import inspect

__all__ = ["test", "mark"]


class Coverage:
    def __init__(self, n_branches: int) -> None:
        self.n_branches: int = n_branches
        self.covered_branches: List[bool] = n_branches * [False]

    def get_coverage(self) -> int:
        return self.covered_branches.count(True) * 100 // self.n_branches

    def get_missing(self) -> str:
        missing = [str(branch_id) for branch_id, covered in enumerate(self.covered_branches) if covered is False]
        return " ".join(missing)


coverages: Dict[str, Coverage] = dict()


def test(n_branches: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        coverages[func.__name__] = Coverage(n_branches)
        return func

    return decorator


def mark(branch_id: int) -> None:
    for frame in inspect.stack():
        if frame.function in coverages:
            coverage = coverages[frame.function]

            coverage.covered_branches[branch_id] = True
            break


def print_table() -> None:
    header = ["Function", "Branch %", "Branches", "Missing"]
    rows = [
        (func_name, coverage.get_coverage(), coverage.n_branches, coverage.get_missing())
        for func_name, coverage in coverages.items()
    ]

    print(tabulate(rows, header))
