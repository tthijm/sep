from typing import List


class Benchmark:
    def __init__(self, amount_of_branches: int) -> None:
        self.amount_of_branches: int = amount_of_branches
        self.reached_branches: List[bool] = amount_of_branches * [False]

    def mark(self, branch_id: int) -> None:
        self.reached_branches[branch_id] = True

    def is_valid(self, branch_id: int) -> bool:
        return 0 <= branch_id < self.amount_of_branches

    def get_coverage(self) -> int:
        return self.reached_branches.count(True) * 100 // self.amount_of_branches

    def get_missing(self) -> str:
        missing = [str(i) for i, v in enumerate(self.reached_branches) if v is False]
        return " ".join(missing)
