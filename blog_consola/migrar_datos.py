from blog.modelos import Autor, Post, Blog
from blog.datos import guardar_datos

# 1. Extracción (Extract): Tu información antigua
perfil_autor = {
    "nombre": "Ana Gómez",
    "rol": "Data Scientist",
    "email": "ana@ejemplo.com"
}

posts_antiguos = [
    {
        "id": 1,
        "titulo": "Introducción a Data Science",
        "contenido": "El análisis de datos nos permite extraer valor...",
        "autor": perfil_autor,
        "tags": ["datos", "python"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Mejores prácticas en SQL",
        "contenido": "Las Window Functions son vitales para...",
        "autor": perfil_autor,
        "tags": ["sql", "datos"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "", 
        "contenido": "Contenido de prueba",
        "autor": "Juan Pérez", 
        "estado": "en_revision" 
    }
]

def ejecutar_migracion():
    mi_blog = Blog()
    print("Iniciando migración de datos...")

    # 2. Transformación (Transform): Limpieza y normalización
    for p in posts_antiguos:
        # A. Normalizar el Autor (Manejo del caso "Juan Pérez" vs Diccionario)
        if isinstance(p["autor"], dict):
            # Usamos el rol como bio, ya que tu clase Autor pedía 'bio'
            autor_obj = Autor(nombre=p["autor"]["nombre"], bio=p["autor"]["rol"])
        else:
            # Si es solo un string escalar, lo convertimos a objeto Autor
            autor_obj = Autor(nombre=p["autor"], bio="Sin biografía")

        # B. Normalizar el Título (Limpieza de nulos/vacíos)
        titulo_limpio = p["titulo"] if p["titulo"] else "Sin Título (Generado Automáticamente)"

        # C. Normalizar Tags (El post 3 no tiene tags en el dict original)
        tags_limpios = p.get("tags", ["sin_etiqueta"])

        # Instanciamos el objeto Post con la data limpia
        nuevo_post = Post(
            id_post=p["id"],
            titulo=titulo_limpio,
            contenido=p["contenido"],
            autor=autor_obj, # Aquí pasamos la instancia, no el string
            tags=tags_limpios,
            estado=p["estado"]
        )
        
        # 3. Carga en memoria (Load)
        mi_blog.agregar_post(nuevo_post)

    # 4. Persistencia física en JSON
    guardar_datos(mi_blog)
    print("Migración completada exitosamente. Tu archivo posts.json ha sido generado.")

if __name__ == "__main__":
    ejecutar_migracion()