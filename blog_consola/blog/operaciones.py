# blog/operaciones.py

def listar_posts(lista):
    """Recorre la lista y muestra título y autor de cada post."""
    print("\n--- LISTA DE POSTS ---")
    if not lista:
        print("No hay posts para mostrar.")
        return

    for post in lista:
        titulo = post.get("titulo", "Sin título")
        autor_dict = post.get("autor", {})
        
        if isinstance(autor_dict, dict):
            nombre_autor = autor_dict.get("nombre", "Autor desconocido")
        else:
            nombre_autor = "Autor con formato incorrecto"
            
        print(f"- '{titulo}' por {nombre_autor}")


def buscar_por_titulo(lista, termino):
    """Busca posts cuyo título contenga el término (case-insensitive)."""
    print(f"\n--- RESULTADOS PARA: '{termino}' ---")
    termino = termino.lower()
    encontrados = False
    
    for post in lista:
        titulo = post.get("titulo", "")
        if termino in titulo.lower() and titulo != "":
            print(f"- Encontrado: {titulo}")
            encontrados = True
            
    if not encontrados:
        print("No se encontraron publicaciones con ese término.")


def filtrar_por_tag(lista, tag):
    """Filtra y muestra posts que contengan el tag indicado."""
    print(f"\n--- POSTS CON TAG: '{tag}' ---")
    tag = tag.lower()
    encontrados = False
    
    for post in lista:
        tags_post = post.get("tags", [])
        tags_lower = [t.lower() for t in tags_post if isinstance(t, str)]
        
        if tag in tags_lower:
            print(f"- {post.get('titulo', 'Sin título')}")
            encontrados = True
            
    if not encontrados:
        print("No se encontraron publicaciones con esa etiqueta.")