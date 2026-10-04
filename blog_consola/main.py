from blog.modelos import Blog, Autor, Post
from blog.datos import cargar_datos, guardar_datos

def main():
    mi_blog = Blog()
    cargar_datos(mi_blog)

    while True:
        print("\n--- MENU DEL BLOG ---")
        print("1. Ver todos los posts")
        print("2. Buscar por titulo")
        print("3. Filtrar por tag")
        print("4. Crear nuevo post")
        print("5. Guardar posts en JSON")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            posts = mi_blog.listar_posts()
            if not posts:
                print("No hay posts para mostrar.")
            else:
                for p in posts:
                    print(f"- {p.titulo} | Autor: {p.autor.nombre} | Estado: {p.estado}")
                
        elif opcion == "2":
            titulo = input("Ingresa el título a buscar: ")
            para_mostrar = mi_blog.buscar_por_titulo(titulo)
            if not para_mostrar:
                print("No se encontraron publicaciones con ese título.")
            else:
                for p in para_mostrar:
                    print(f"- {p.titulo} | Autor: {p.autor.nombre} | Estado: {p.estado}")

        elif opcion == "3":
            tag = input("Ingresa el tag a filtrar: ")
            para_mostrar = mi_blog.filtrar_por_tag(tag)
            if not para_mostrar:
                print("No se encontraron publicaciones con esa etiqueta.")
            else:
                for p in para_mostrar:
                    print(f"- {p.titulo} | Autor: {p.autor.nombre} | Estado: {p.estado}")
            
        elif opcion == "4":
            print("\nCreando nuevo post...")
            nombre_autor = input("Nombre del autor: ")
            bio_autor = input("Bio del autor: ")
            titulo = input("Título del post: ")
            contenido = input("Contenido: ")
            tags = input("Tags (separados por coma): ").split(",")
            
            # Composición en acción
            nuevo_autor = Autor(nombre_autor, bio_autor)
            nuevo_post = Post(len(mi_blog.posts)+1, titulo, contenido, nuevo_autor, [t.strip() for t in tags])
            
            mi_blog.agregar_post(nuevo_post)
            print("Post creado en memoria.")
            
        elif opcion == "5":
            guardar_datos(mi_blog)
            print("Posts guardados en JSON exitosamente.")
            
        elif opcion == "6":
            # Opcional: Autoguardado al salir
            guardar_datos(mi_blog)
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 6.")

if __name__ == "__main__":
    main()