# README #
python3 --version
Python 3.8.10

El código esta divido en tres archivos:

* main.py: Archivo principal que ejecuta el programa.

* lexico.py: Contiene las funciones relacionadas con el análisis léxico (tokenización).

* sintactico.py: Contiene las funciones relacionadas con el análisis sintáctico (interpretación y ejecución de comandos).

* Script: archivos con errores lexicos, sintacticos y script con la sintaxis del codigo. 


# COMPILAR #
python3 main.py


# ERRORES LEXICOS #

Errores :
1. CURSO(1,MATE); *
El carácter * no parece seguir la sintaxis esperada. Si * no está definido como un token válido en la gramática, esto se consideraría un error léxico.
2. ESTUDIANTE(1,JOS*E,1);
La presencia de * en JOS*E podría ser un error léxico si el asterisco no está permitido en los nombres o strings.
3. EST UDIANTE(2,PEDRO,1);
La separación de EST y UDIANTE por múltiples espacios podría llevar a un error léxico, ya que el analizador podría no reconocerlo como el token esperado ESTUDIANTE.


# ERRORES SINTACTICOS #

1. CURSO(1,MATE); *
Además de ser un posible error léxico, la inclusión de * también podría ser un error sintáctico si no hay una regla en la gramática que permita un carácter * después de un punto y coma.
2. EST UDIANTE(2,PEDRO,1);
Asumiendo que ESTUDIANTE es la palabra clave correcta, la fragmentación de la palabra clave puede ser interpretada como un error sintáctico.
3. Curso(3,estadistica);
Si la gramática requiere que CURSO esté en mayúsculas, el uso de Curso podría ser considerado un error sintáctico.
4. Estudiante(3,jo,2);
Igual que el anterior, si la gramática distingue entre mayúsculas y minúsculas, el uso de Estudiante en lugar de ESTUDIANTE sería un error.

# USO #
El archivo main.py buscar la variable filepath, cambiar por la ruta del archivo que desea ejecutar o hacia los archivos del directorio # Scripts # del proyecto.

    filepath = "/home/ferdynandcv/Documents/Projects/Compilador/Scritpts/script.std"

Una vez que el script esté cargado, puedes interactuar con el intérprete a través de los comandos:

set breakpoint <no_linea> : Asignar un punto de ruptura en una línea específica.
  
del breakpoint <no_linea> : Eliminar un punto de ruptura existente.

print <ESTUDIANTE> : Imprimir la información de un estudiante específico.

run : Continuar la ejecución hasta el próximo breakpoint o hasta el fin del script.

step : Ejecutar el programa paso a paso, instrucción por instrucción.

stop : Detener la ejecución del programa y salir.




