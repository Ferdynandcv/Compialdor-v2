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

    def execute(self, command):
        parts = command.split('(')
        command_name = parts[0].strip()
        if command_name == "CURSO":
            params = parts[1].split(',')
            course_id = int(params[0])
            course_name = params[1].strip()[:-1]  # Eliminar el paréntesis final
            self.courses[course_id] = Course(course_id, course_name)
        elif command_name == "ESTUDIANTE":
            params = parts[1].split(',')
            student_id = int(params[0])
            student_name = params[1].strip()
            course_id = int(params[2][:-1])  # Eliminar el paréntesis final
            self.students[student_id] = Student(student_id, student_name, course_id)
        elif command_name == "Buscar_estudiante":
            student_id = int(parts[1][:-1])  # Eliminar el paréntesis final
            print(self.students.get(student_id, "Estudiante no encontrado"))
        elif command_name == "Eliminar_estudiante":
            student_id = int(parts[1][:-1])  # Eliminar el paréntesis final
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

