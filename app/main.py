import sys

def main():
    Commands = {"exit", "echo", "type"}
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()
        if command == "exit 0":
            sys.exit()
        elif command.split(" ")[0] == "echo":
            msg = command.split("echo")[1]
            print(f"{msg}")
        elif command.split(" ")[0] == "type":
            #cmd = command.split("type")[1].strip()
            if commmand.split(" ")[1] in Commands:
                print(f"{cmd} is a shell builtin")
            else:
                print(f"{cmd}: command not found")
        else: 
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
