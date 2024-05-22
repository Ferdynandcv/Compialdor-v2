def tokenize(command):
    parts = command.split('(')
    command_name = parts[0].strip()
    params = parts[1].strip()[:-1].split(',')
    return command_name, params
