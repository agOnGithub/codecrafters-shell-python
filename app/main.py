import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()
        if command == "exit 0":
            sys.exit()
        elif command.split(" ")[0] == "echo":
            msg = command.split("echo")[0]
            print(msg)
        else: 
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
