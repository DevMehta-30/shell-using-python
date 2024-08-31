import sys
import os

def main():
    # Uncomment this block to pass the first stage
    PATH=os.environ.get("PATH")
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        if command := input().strip():
            if command == "exit 0":
                sys.exit(0)
            elif command.startswith("echo "):
                print(command[len("echo ") :])
            elif command.startswith("type "):
                s=command[len("type "):]
                cmd_path=None
                paths=PATH.split(":")
                for path in paths:
                    if os.path.isfile(f"{path}/{s}"):
                        cmd_path = f"{path}/{s}"
                if s in ["echo","exit","type"]:
                    print(f"{s} is a shell builtin")
                elif cmd_path:
                    print(f"{s} is {cmd_path}")
                else:
                    print(f"{s}: not found")
            else:
                if os.path.isfile(command.split(" ")[0]):
                    os.system(command)
                else:
                    print(f"{command}: command not found")



if __name__ == "__main__":
    main()
