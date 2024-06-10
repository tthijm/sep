from typing import List


class Benchmark:
    def __init__(self, amount_of_branches: int) -> None:
        self.amount_of_branches: int = amount_of_branches
        self.reached_branches: List[bool] = amount_of_branches * [False]

    def mark(self, branch_id: int) -> None:
        self.reached_branches[branch_id] = True

    def is_valid(self, branch_id: int) -> bool:
        return 0 <= branch_id < self.amount_of_branches
