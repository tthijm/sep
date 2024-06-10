import sys, subprocess
from utils import results


def main() -> None:
    arguments = sys.argv

    subprocess.run(arguments[1:])
    print(results) # <--


if __name__ == "__main__":
    main()
