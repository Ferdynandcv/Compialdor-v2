from lexico import tokenize

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_name):
        self.students = [s for s in self.students if s.name != student_name]

    def __str__(self):
        return f"ID: {self.course_id}, CURSO: {self.name}, ESTUDIANTE: {[student.name for student in self.students]}"

class Student:
    def __init__(self, student_id, name, course_id):
        self.student_id = student_id
        self.name = name
        self.course_id = course_id

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Course ID: {self.course_id}"

class ScriptInterpreter:
    def __init__(self):
        self.courses = {}
        self.students = {}
        self.breakpoints = set()
        self.current_line = 0
        self.stopped = False

    def execute(self, command):
        if self.stopped:
            print("Programa detenido.")
            return

        command_name, params = tokenize(command)
        
        if command_name == "CURSO":
            course_id = int(params[0])
            course_name = params[1].strip()
            self.courses[course_id] = Course(course_id, course_name)
        elif command_name == "ESTUDIANTE":
            student_id = int(params[0])
            student_name = params[1].strip()
            course_id = int(params[2])
            self.students[student_id] = Student(student_id, student_name, course_id)
        elif command_name == "Buscar_estudiante":
            student_id = int(params[0])
            print(self.students.get(student_id, "Estudiante no encontrado"))
        elif command_name == "Eliminar_estudiante":
            student_id = int(params[0])
            if student_id in self.students:
                del self.students[student_id]
                print("Estudiante eliminado correctamente")
            else:
                print("Estudiante no encontrado")
        elif command_name == "Mostrar_estudiante":
            for student_id, student in self.students.items():
                print(student)
        elif command_name == "mostrar_curso":
            for course_id, course in self.courses.items():
                print(course)
        elif command_name == "set breakpoint":
            line_number = int(params[0])
            self.breakpoints.add(line_number)
            print(f"Punto de ruptura establecido en la línea {line_number}")
        elif command_name == "del breakpoint":
            line_number = int(params[0])
            if line_number in self.breakpoints:
                self.breakpoints.remove(line_number)
                print(f"Punto de ruptura eliminado en la línea {line_number}")
            else:
                print(f"No hay ningún punto de ruptura en la línea {line_number}")
        elif command_name == "print":
            student_id = int(params[0])
            print(self.students.get(student_id, "Estudiante no encontrado"))
        elif command_name == "run":
            if len(params) > 0:
                line_number = int(params[0])
                self.current_line = line_number
            self.stopped = True
        elif command_name == "step":
            self.current_line += 1
            self.stopped = True
        elif command_name == "stop":
            self.stopped = True
