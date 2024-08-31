import sys
import os

def find_in_path(param):
    path = os.environ['PATH']
    print("Path: " + path)
    print(f"Param: {param}")
    for directory in path.split(":"):
        for (dirpath, dirnames, filenames) in os.walk(directory):
            if param in filenames:
                return f"{dirpath}/{param}"
    return None

# def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        if command := input():
            if command == "exit 0":
                sys.exit(0)
            elif command.startswith("echo "):
                print(command[len("echo ") :])
            elif command.startswith("type "):
                s=command[len("type "):]
                location=find_in_path(s)
                if s in ["echo","exit","type"]:
                    print(f"{s} is a shell builtin")
                elif location:
                    print(f"{s} is {location}")
                else:
                    print(f"{s}: not found")
            else:
                if os.path.isfile(command.split(" ")[0]):
                    os.system(command)
                else:
                    print(f"{command}: command not found")

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        match command.split(" "):
            case ["exit", "0"]:
                exit(0)
            case ["echo", *cmd]:
                print(" ".join(cmd))
            case ["type", *cmd]:
                match cmd:
                    case ["echo" | "exit" | "type"]:
                        print(f"${cmd[0]} is a shell builtin")
                    case _:
                        location = find_in_path(cmd[0])
                        if location:
                            print(f"${cmd[0]} is {location}")
                        else:
                            print(f"${" ".join(cmd)} not found")
            case _:
                if os.path.isfile(command.split(" ")[0]):
                    os.system(command)
                else:
                    print(f"{command}: command not found")

if __name__ == "__main__":
    main()
