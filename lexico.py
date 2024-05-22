def tokenize(command):
    parts = command.split('(')
    command_name = parts[0].strip()
    params = [param.strip() for param in parts[1].strip()[:-1].split(',')]  # Agregar strip() para eliminar espacios en blanco alrededor de los parámetros
    return command_name, params
