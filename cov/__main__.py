import sys
import pytest
from cov.utils import results


def main() -> None:
    arguments = sys.argv

    pytest.main(arguments[1:])
    print(results)


if __name__ == "__main__":
    main()
