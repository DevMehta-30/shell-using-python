import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_command = input()
        if user_command == "exit 0":
            break



if __name__ == "__main__":
    main()
