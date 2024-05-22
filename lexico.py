
import re

class LexicalError(Exception):
    def __init__(self, message):
        super().__init__(message)

class SyntaxError(Exception):
    def __init__(self, message):
        super().__init__(message)

def tokenize(command):
    if not command.endswith(");"):
        raise LexicalError("El comando debe terminar con ');'")

    parts = command[:-2].split('(')
    if len(parts) != 2:
        raise LexicalError("El comando debe contener un nombre de comando y parámetros entre paréntesis")

    command_name = parts[0].strip()
    params = parts[1].split(',')

    # Verificación de errores léxicos específicos
    if not re.match(r'^[A-Za-z_]+$', command_name):
        raise LexicalError(f"El nombre del comando '{command_name}' contiene caracteres no válidos o está mal formado")
    for param in params:
        if '*' in param:
            raise LexicalError(f"El parámetro '{param}' contiene un carácter no válido '*'")

    command_name = ''.join(command_name.split())  # Eliminar espacios adicionales en el nombre del comando

    return command_name, [param.strip() for param in params if param.strip()]

