import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        if command == "exit 0":
            sys.exit(0)
        first_part, rest = command.split(None, 1)
        if first_part == "echo":
            print(rest)
        print(f"{command}: command not found")



if __name__ == "__main__":
    main()
