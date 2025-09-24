import datetime
class Fecha:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

class Libro:
    def __init__(self, titulo, autor, categoria):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponible = True

class Usuario:
    def __init__(self, nombre, id_usuario, correo):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.correo = correo

class Autor:
    def __init__(self, nombre, libro):
        self.nombre = nombre
        self.libro = libro

class Categoria:
    def __init__(self, libro, tipo):
        self.libro =libro
        self. tipo = tipo


class Prestamo:
    def __init__(self, usuario, libro, fecha, cobro):
        self.usuario = usuario
        self.libro = libro
        self.fecha = fecha
        self.cobro = cobro

#almacen porsi acaso no me acuerdo lo que es :D

libros = []
usuarios = []
prestamos = []
autores = []
categorias = []

while True:
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Registrar autor")
    print("4. Registrar categoría")
    print("5. Registrar préstamo")
    print("6. Mostrar libros")
    print("7. Mostrar usuario")
    print("8. Mostrar préstamos")
    print("9. Salir")

    opcion = input("ingresa tu opcion: ")
    if opcion == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("tipo de categoria: ")
        libro =Libro(titulo, autor, categoria)
        libros.append(libro)
        print(">> libro registrado con exito:D <<")
    
    elif opcion == "2":
        nombre = input("cual es tu nombre: ")
        id_usuario = input("cual es tu id: ")
        correo = input("ingresa tu correo electronico: ")
        usuario =Usuario(nombre, id_usuario, correo)
        usuarios.append(usuario)
        print(">> usuario registrado Bienvenido al imalaya:D <<")

    elif opcion == "3":
        nombre = input("cual es el nombre del autor: ")
        libro = input("que libro escribio ese autor: ")
        autor = Autor(nombre, libro)
        autores.append(autor)
        print(">>autor registrado con exito<<")

    elif opcion == "4":
       libro = input("cual es el libro: ")
       tipo = input("cual es cu categoria: ")
       categoria = Categoria(libro, tipo)
       categorias.append(categoria)
       print(">> categoria puesta <<")

    elif opcion == "5":
        libro = input("cual es el libro: ")