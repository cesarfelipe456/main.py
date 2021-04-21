import json
try:
    with open("base_de_datos.json", "y") as archivo_db:
        print("Cargando la base de datos.")
        catalogo_estudiantes = json.load(archivo_db)
        print("La base de datos a cargado correctamente")
except:
    print("se esta creando una nueva base de datos correspondiente")
    catalogo_estudiantes = []
#
def mostrar_menu():
    mensaje_menu = """Bienvenido puede Ingresar la opcion que desea ejecutar\n
    ************************ le presentamos acontinuacion estas opciones que desea utilizar*******************\n
                ******************************************************************************
                        ************************************************************
                                 ******************************************
                                            *********************
                                                 **********

    1. Desea ver los datos de los estudiantes.\n
    2. Se le mostrara la cantidad de los estudiaantes que estan en registro.\n
    3. Si desea registrar un nuevo estudiante sera esta la opcion.\n
    0. Salir\n
                                                 ***********
                                            ***********************
                                  *****************************************
                         ***********************************************************
                ********************************************************************************
    ***********************************************************************************************************\n
                
    > 
    """
    opcion = input(mensaje_menu)
    opcion = int(opcion)

    if opcion == 1:
        mostrar_catalogo_estudiantes()
        
    if opcion == 2:
        mostrar_cantidad_estudiantes()
    
    if opcion == 3:
        ingresar_nuevo_estudiante()
        
    if opcion == 0:
        
        with open("base_de_datos.json", "w") as archivo_db:
            print("Guardando toda la base de datos...")
            json.dump(catalogo_estudiantes, archivo_db)
        return
    mostrar_menu()
    return

#

def calcular_promedio(lista_calificaciones_estudiantes):
    total_suma = 0
    
    for nota in lista_calificaciones_estudiantes:
        total_suma = total_suma + nota
    
    cantidad_notas = len(lista_calificaciones_estudiantes)
    
    promedio = total_suma / cantidad_notas
    
    return promedio

def ingresar_nuevo_estudiante():
    
    nombre = input("ingrese nuevo nombre por favor  ")
    anno_ingreso = input('Ingresa el anno de ingreso: ')
    correlativo = 100
    identificator = format(id(correlativo), 'x')
    print(anno_ingreso)
    print(identificator)
    carnet = input("Ingrese carnet: ")
    curso = input("A cuantos cursos desea ingresar:")  
   
#

#

    lista_notas = []
    opcion_notas = input("esta deacuerdo en ingresar una nota? (s / n): ")
    while opcion_notas == 's' or opcion_notas == 's':
        nueva_nota = input("Ingrese la nota correspondiente: ")
        
        nueva_nota = int(nueva_nota)
        lista_notas.append(nueva_nota)
        opcion_notas = input("esta deacuerdo en ingresar otra nota? (s / n): ")
    
    
    promedio = calcular_promedio(lista_notas)
    
    estudiante = {
        "1: **nombre\n": nombre,
        "2: **numero de carnet\n": carnet,
        "'3: **total de notas\n": lista_notas,
        "4: **un promedio de\n:": promedio,
        "5: **cursos asignados:\n": curso,
        "6: **anno de ingreso\n":anno_ingreso,
        "7: **su identifiador es:":identificator,

    }
    
    catalogo_estudiantes.append(estudiante)
    return

def mostrar_catalogo_estudiantes():
    print(catalogo_estudiantes)
    return

def mostrar_cantidad_estudiantes():
    cifra = len(catalogo_estudiantes)
    print(f'son {cifra} estudiantes los que estan registrados actualmente')
    return

mostrar_menu()