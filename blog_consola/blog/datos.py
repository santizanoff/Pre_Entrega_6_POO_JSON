import json
import os
from blog.modelos import Post

RUTA_JSON = "posts.json"

def cargar_datos(blog):
    # Manejo de error: Si el archivo no existe, iniciamos con la lista vacía
    if not os.path.exists(RUTA_JSON):
        return 

    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as file:
            datos = json.load(file)
            for item in datos:
                post = Post.from_dict(item)
                blog.agregar_post(post)
    except json.JSONDecodeError:
        # Manejo de error: Archivo corrupto o vacío
        print("El archivo posts.json está vacío o inválido. Iniciando sin datos previos.")
    except Exception as e:
        print(f"Error crítico al cargar la base de datos: {e}")

def guardar_datos(blog):
    try:
        # Transformamos toda la lista de objetos Post a diccionarios
        datos_serializados = [post.to_dict() for post in blog.posts]
        with open(RUTA_JSON, "w", encoding="utf-8") as file:
            json.dump(datos_serializados, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al persistir los datos en JSON: {e}")