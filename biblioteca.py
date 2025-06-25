def buscar_rut_de_usuario(rut,usuario):
    for usuario in usuarios:
        if usuario["rut"]== rut:
            return usuario
    return None

def cantidad_libros_disponibles(libros):
    for libro in libros:
        if libro["cantidad_disponible"] > 0 :
            print(f"{libro['id']}-{libro['titulo']} ({libro['cantidad_disponible']} disponibles)")
        else:
            print("No hay stock de este libro.")
            
def prestamos_de_libro(usuario, libros):
    cantidad_libros_disponibles(libros)
    try :
        id_libro=int(input("Ingrese la ID del libro que desea: "))
        for libro in libros: 
            if libro["id"]== id_libro and libro["cantidad_disponible"]>0 : 
                usuario["libros"].append(id_libro)
                libro["cantidad_disponible"]-=1
                print(f"Se realizó exitosamente el prestamo del libro: {libro['titulo']}")
                return
        print("Este libro no esta disponible")                   
    except ValueError as errorrr:
        print(errorrr)
        print("error funcion prestamo")    
  
def devolucion_de_libro(usuario, libros):
    try : 
        id_libro = int(input("Ingresa la id  del libro que desee devolver : "))
        if id_libro in usuario["libros"]:
            for libro in libros :
                if libro["id"]== id_libro:
                    libro["cantidad_disponible"]+=1
                    usuario["libros"].remove(id_libro)
                    print(f"Se devolvio con exito el libro : {libro['titulo']}")
                    return
        else:
            print("el libro no pertenece a este usuario, o este usuario no tiene ningun libro en su poder.")
    except ValueError as error: 
        print(f"{error}, error en devolucion")
                    
            
def registrar_usuario(usuarios):
    nombre=input("Ingrese el nombre del nuevo usuario: ")
    apellido=input("ingrese el apellido del nuevo usuario: ")
    rut=input("ingrese el rut del nuevo usuario: ")
    nuevo_usuario = {"nombre": nombre, "apellido": apellido, "rut": rut, "libros": [] } 
    usuarios.append(nuevo_usuario)
    print(f"Se registro con exito el nuevo usuario.")

def registrar_libro(libros):
    titulo = input("Ingrese el título del libro: ").title()
    autor = input("Ingrese el autor: ")
    isbn = input("Ingrese el ISBN: ")
    try: 
        paginas = int(input("Ingrese el número de páginas: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
    except ValueError as errorentero: 
        print("error (entero)", errorentero)
    nuevo_libro= {
        "id": len(libros) + 1,
        "titulo": titulo,
        "autor": autor,
        "ISBN": isbn,
        "paginas": paginas,
        "cantidad_disponible": cantidad
        }
    libros.append(nuevo_libro)
    print("se añadio un libro exitosamente")
    
  
usuarios = [
    {"nombre": "Ana", "apellido": "González", "rut": "13816108-7", "libros": []},
    {"nombre": "Luis", "apellido": "Rodríguez", "rut": "13872719-2", "libros": []},
    {"nombre": "Camila", "apellido": "Pérez", "rut": "12182343-5", "libros": []},
    {"nombre": "Jorge", "apellido": "Muñoz", "rut": "14044461-9", "libros": []},
    {"nombre": "María", "apellido": "Rojas", "rut": "16149391-0", "libros": []},
    {"nombre": "Diego", "apellido": "Díaz", "rut": "10407062-4", "libros": [0]},
    {"nombre": "Lucía", "apellido": "Soto", "rut": "19306158-3", "libros": []},
    {"nombre": "Pablo", "apellido": "Torres", "rut": "14864522-5", "libros": []},
    {"nombre": "Valentina", "apellido": "Contreras", "rut": "15592214-1", "libros": []},
    {"nombre": "Tomás", "apellido": "Silva", "rut": "10516040-5", "libros": []}
]

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "ISBN": "978-0307474728", "paginas": 432, "cantidad_disponible": 5},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "ISBN": "978-0451524935", "paginas": 328, "cantidad_disponible": 3},
    {"id": 3, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ISBN": "978-1451673319", "paginas": 194, "cantidad_disponible": 7},
    {"id": 4, "titulo": "Don Quijote", "autor": "Miguel de Cervantes", "ISBN": "978-0060934347", "paginas": 992, "cantidad_disponible": 2},
    {"id": 5, "titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "ISBN": "978-1400034956", "paginas": 128, "cantidad_disponible": 4},
    {"id": 6, "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "ISBN": "978-0156013987", "paginas": 96, "cantidad_disponible": 10},
    {"id": 7, "titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "ISBN": "978-0156007757", "paginas": 352, "cantidad_disponible": 3},
    {"id": 8, "titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "ISBN": "978-0143034902", "paginas": 512, "cantidad_disponible": 6},
    {"id": 9, "titulo": "El túnel", "autor": "Ernesto Sabato", "ISBN": "978-9500420305", "paginas": 160, "cantidad_disponible": 2},
    {"id": 10, "titulo": "Pedro Páramo", "autor": "Juan Rulfo", "ISBN": "978-6073142360", "paginas": 144, "cantidad_disponible": 8}
]
print("*********Programa: Sistema de Biblioteca*********")
while True: 
    print('''----------MENU----------
    1 - Buscar usuarios
    2 - Registrar un usuario
    3 - Registrar un libro
    4.- Salir
          ''')
    try: 
        opcinon=int(input("ingrese la opcion que desee: "))
    except ValueError as error : 
        print(f"{error}, intentelo de nuevo")
    if opcinon ==4 : 
        print("Gracias por usar el programa, ¡Hasta la Proxima!")
        break
    if opcinon== 1 : 
        rut=input("para buscar usuario, debe ingresar su rut: ")
        usuario = buscar_rut_de_usuario(rut, usuarios)
        if usuario:
            print(f"Usuario encontrado: {usuario['nombre']} {usuario['apellido']}")
            while True: 
                print('''
                      ---MENU USUARIO---
                      1)realizar el prestamo de un libro
                      2)realizar la devulucion de un libro
                      3)salir al menu principal
                      ''')
                try: 
                    subopcion=int(input("ingrese la opcion que desee: "))
                except ValueError as error2 :
                    print(error2, "error intentelo de nuevo")
                if subopcion==3 :
                    break
                elif subopcion== 1 : 
                    prestamos_de_libro(usuario,libros)
                elif subopcion == 2 :
                    devolucion_de_libro(usuario, libros)
    elif opcinon==2:
        registrar_usuario(usuarios)
    elif opcinon==3 :
        registrar_libro(libros)