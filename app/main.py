import sys
import os
from os import chdir
from os.path import expanduser

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
                if s in ["echo","exit","type","pwd","cd"]:
                    print(f"{s} is a shell builtin")
                elif cmd_path:
                    print(f"{s} is {cmd_path}")
                else:
                    print(f"{s}: not found")
            elif command=="pwd":
                print(os.getcwd())
            elif command=="cd":
                d=command[3:]
                try:
                    chdir(expanduser(d))
                except OSError:
                    print(f"cd: {d}: No such file or directory")
            else:
                if command.startswith('my_exe'):
                    os.system(command)
                else:
                    print(f"{command}: command not found")



if __name__ == "__main__":
    main()
