import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        first_part, rest = command.split(None, 1)
        if first_part == "echo":
            print(rest)
            


if __name__ == "__main__":
    main()
