# import sys
# import os
# from os import chdir
# from os.path import expanduser
# from subprocess import call

# def main():
#     # Uncomment this block to pass the first stage
#     PATH=os.environ.get("PATH")
#     while True:
#         sys.stdout.write("$ ")
#         sys.stdout.flush()
#         if command := input().strip():
#             if command == "exit 0":
#                 sys.exit(0)
#             elif command.startswith("echo "):
#                 print(command[len("echo ") :])
#             elif command.startswith("type "):
#                 s=command[len("type "):]
#                 cmd_path=None
#                 paths=PATH.split(":")
#                 for path in paths:
#                     if os.path.isfile(f"{path}/{s}"):
#                         cmd_path = f"{path}/{s}"
#                 if s in ["echo","exit","type","pwd","cd"]:
#                     print(f"{s} is a shell builtin")
#                 elif cmd_path:
#                     print(f"{s} is {cmd_path}")
#                 else:
#                     print(f"{s}: not found")
#             elif command=="pwd":
#                 print(os.getcwd())
#             elif command=="cd":
#                 d=command[3:]
#                 try:
#                     chdir(expanduser(d))
#                 except OSError:
#                     print(f"cd: {d}: No such file or directory")
#             elif command.startswith("/"):
#                     call("{}".format(command), shell=True)
#             else:
#                 if command.startswith('my_exe'):
#                     os.system(command)
#                 else:
#                     print(f"{command}: command not found")



# if __name__ == "__main__":
#     main()
from os.path import basename, expanduser
from os import getenv, getcwd, chdir
from subprocess import call
from typing import Dict
from glob import glob


def collect_executables() -> Dict[str, str]:
    executables = {}

    for directory in getenv('PATH').split(':'):
        executables.update({
            basename(executable): directory for executable in glob(directory + '/*') if basename(executable) not in executables
        })

    return executables


def main() -> None:
    executables = collect_executables()
    originalwd = getcwd()

    while True:
        try:
            line = input('$ ').split(' ')

            if not line:
                print('Could not parse input')
            else:
                command, arguments = line[0], line[1:]

                if command == 'exit':
                    exit(
                        int(arguments[0]) if arguments else 0
                    )
                elif command == 'echo':
                    print(' '.join(arguments))
                elif command == 'type':
                    target = arguments[0] if arguments else None

                    if target in ('exit', 'echo', 'type', 'pwd', 'cd'):
                        print(f'{target} is a shell builtin')
                    else:
                        directory = executables.get(target)

                        if directory:
                            print(f'{target} is {directory}/{target}')
                        else:
                            print(f'{target} not found')
                elif command == 'pwd':
                    print(getcwd())
                elif command == 'cd':
                    directory = arguments[0]

                    try:
                        chdir(expanduser(directory))
                    except OSError:
                        print(f'cd: {directory}: No such file or directory')
                elif command.startswith('/'):
                    call(
                        '{} {}'.format(
                            command,
                            ' '.join(arguments)
                        ),
                        shell=True
                    )
                else:
                    directory = executables.get(command)

                    if directory:
                        call(
                            '{}/{} {}'.format(
                                directory,
                                command,
                                ' '.join(arguments)
                            ),
                            shell=True
                        )
                    else:
                        print(f'{command}: command not found')
        except (KeyboardInterrupt, EOFError):
            exit(130)

    exit(0)


if __name__ == '__main__':
    main()