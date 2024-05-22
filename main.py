from sintactico import ScriptInterpreter

def main():
    interpreter = ScriptInterpreter()
    while True:
        try:
            command = input(">>> ")
            if command.lower() in ["exit", "quit"]:
                break
            interpreter.execute(command)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
