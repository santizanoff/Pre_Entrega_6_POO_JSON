# blog/menu.py

def mostrar_menu():
    """
    Muestra el menú interactivo y maneja errores de entrada.
    Retorna la opción elegida como entero o -1 si hay error.
    """
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    
    try:
        opcion = int(input("Elige una opción: "))
        return opcion
    except ValueError:
        return -1