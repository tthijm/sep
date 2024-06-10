import sys
import pytest
import cov.utils


def main() -> None:
    arguments = sys.argv

    pytest.main(arguments[1:])
    cov.utils.print_results()


if __name__ == "__main__":
    main()
