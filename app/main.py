import sys
import os

def does_it_exist(path, cmd):
    for folder in path.split(":"):
        if os.path.isfile(f"{folder}/{cmd}"):
            return folder
    return None

def main():
    Commands = {"exit", "echo", "type"}
    path = os.getenv("PATH")
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()
        #PATH="/usr/bin:/usr/local/bin" ./your_shell.sh
        if command == "exit 0":
            sys.exit()
        elif command.split(" ")[0] == "echo":
            msg = command.split("echo")[1]
            print(f"{msg}")
        elif command.split(" ")[0] == "type":
            cmd = command.split(" ")[1].strip()
            if cmd in Commands:
                print(f"{cmd} is a shell builtin")
            else:
                bin_folder = does_it_exist(path, cmd)
                if bin_folder:
                    print(f"{cmd} is {bin_folder}/{cmd}")
                else: 
                    print(f"{cmd}: not found")
        else: 
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
