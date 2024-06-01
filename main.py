# main.py

from sintactico import ScriptInterpreter

def main():
    interpreter = ScriptInterpreter()
    filepath = "/home/ferdynandcv/Documents/Projects/Compilador/Scritpts/script.std"
    interpreter.load_script(filepath)

    # Interacción del usuario
    while True:
        user_input = input("Commands: ")
        parts = user_input.split()
        command_name = parts[0]

        if command_name == "set" and parts[1] == "breakpoint":
            line_number = int(parts[2])
            interpreter.set_breakpoint(line_number)
        elif command_name == "del" and parts[1] == "breakpoint":
            line_number = int(parts[2])
            interpreter.delete_breakpoint(line_number)
        elif command_name == "print" and parts[1] == "ESTUDIANTE":
            student_id = int(parts[2])
            interpreter.execute(f"Buscar_estudiante({student_id});")
        elif command_name == "run":
            interpreter.run()
        elif command_name == "step":
            interpreter.step()
        elif command_name == "stop":
            interpreter.stop()
            break
        else:
            print("unrecognized command")

if __name__ == "__main__":
    main()
