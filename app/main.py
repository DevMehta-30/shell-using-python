import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        if command := input().strip():
            if command == "exit 0":
                sys.exit(0)
            elif command.startswith("echo "):
                print(command[len("echo ") :])
            else:
                print(f"{command}: command not found")



if __name__ == "__main__":
    main()
