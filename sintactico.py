# sintactico.py

from lexico import tokenize, LexicalError, SyntaxError

class Student:
    def __init__(self, student_id, name, course_id):
        self.student_id = student_id
        self.name = name
        self.course_id = course_id

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Course ID: {self.course_id}"

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.course_name}"

class ScriptInterpreter:
    def __init__(self):
        self.courses = {}
        self.students = {}
        self.breakpoints = set()
        self.running = False
        self.commands = []
        self.current_line = 0

    def load_script(self, filepath):
        try:
            with open(filepath, 'r') as file:
                script = file.read()
            self.commands = script.strip().split('\n')
            self.current_line = 0
            print(f"Script {filepath} loaded successfully.")
        except FileNotFoundError:
            print(f"File {filepath} not found.")
        except Exception as e:
            print(f"Error loading script: {e}")

    def execute(self, command):
        try:
            command_name, params = tokenize(command)

            # Verificación de errores sintácticos
            if command_name not in ["CURSO", "ESTUDIANTE", "Buscar_estudiante", "Eliminar_estudiante", "Mostrar_estudiante", "mostrar_curso"]:
                raise SyntaxError(f"Comando '{command_name}' no reconocido.")

            if command_name == "CURSO":
                if len(params) != 2:
                    raise SyntaxError("CURSO requiere 2 parámetros.")
                course_id = int(params[0])
                course_name = params[1].strip()
                self.courses[course_id] = Course(course_id, course_name)
                print(f"Curso '{course_name}' con ID {course_id} añadido correctamente.")

            elif command_name == "ESTUDIANTE":
                if len(params) != 3:
                    raise SyntaxError("ESTUDIANTE requiere 3 parámetros.")
                student_id = int(params[0])
                student_name = params[1].strip()
                course_id = int(params[2].strip())
                self.students[student_id] = Student(student_id, student_name, course_id)
                print(f"Estudiante '{student_name}' con ID {student_id} añadido correctamente al curso {course_id}.")

            elif command_name == "Buscar_estudiante":
                if len(params) != 1:
                    raise SyntaxError("Buscar_estudiante requiere 1 parámetro.")
                student_id = int(params[0].strip())
                student = self.students.get(student_id)
                if student:
                    print(student)
                else:
                    print("Estudiante no encontrado.")

            elif command_name == "Eliminar_estudiante":
                if len(params) != 1:
                    raise SyntaxError("Eliminar_estudiante requiere 1 parámetro.")
                student_id = int(params[0].strip())
                if student_id in self.students:
                    del self.students[student_id]
                    print("Estudiante eliminado correctamente.")
                else:
                    print("Estudiante no encontrado.")

            elif command_name == "Mostrar_estudiante":
                if params:
                    raise SyntaxError("Mostrar_estudiante no requiere parámetros.")
                if self.students:
                    print("Lista de estudiantes:")
                    for student in self.students.values():
                        print(student)
                else:
                    print("No hay estudiantes registrados.")

            elif command_name == "mostrar_curso":
                if params:
                    raise SyntaxError("mostrar_curso no requiere parámetros.")
                if self.courses:
                    print("Lista de cursos:")
                    for course in self.courses.values():
                        print(course)
                else:
                    print("No hay cursos registrados.")

        except (LexicalError, SyntaxError) as e:
            print(f"Error: {e}")

    def run(self):
        self.running = True
        while self.current_line < len(self.commands):
            if self.current_line in self.breakpoints:
                print(f"Breakpoint at line {self.current_line}.")
                break
            self.execute_line()
            if not self.running:
                break

    def execute_line(self):
        if self.current_line < len(self.commands):
            command = self.commands[self.current_line].strip()
            if command:
                print(f"Executing line {self.current_line}: {command}")
                self.execute(command)
            self.current_line += 1

    def step(self):
        if self.current_line < len(self.commands):
            command = self.commands[self.current_line].strip()
            if command:
                print(f"Stepping line {self.current_line}: {command}")
                self.execute(command)
            self.current_line += 1

    def stop(self):
        self.running = False
        print("Execution stopped.")

    def set_breakpoint(self, line_number):
        self.breakpoints.add(line_number)
        print(f"Breakpoint set at line {line_number}")

    def delete_breakpoint(self, line_number):
        if line_number in self.breakpoints:
            self.breakpoints.remove(line_number)
            print(f"Breakpoint at line {line_number} deleted")
        else:
            print(f"No breakpoint found at line {line_number}")

