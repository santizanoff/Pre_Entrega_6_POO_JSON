# blog/validaciones.py

# pyrefly: ignore [missing-import]
from blog.datos import estados_post

def validar_post(post):
    """
    Verifica si un post cumple con todas las reglas de estructura.
    Retorna (True, "Válido") o (False, "Mensaje de error").
    """
    if not isinstance(post, dict):
        return False, "El post no es un diccionario"
        
    claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_obligatorias:
        if clave not in post:
            return False, f"Falta la clave obligatoria '{clave}'"
            
    if not post["titulo"] or str(post["titulo"]).strip() == "":
        return False, "El título está vacío"
        
    if not post["contenido"] or str(post["contenido"]).strip() == "":
        return False, "El contenido está vacío"
        
    if not isinstance(post["autor"], dict):
        return False, "El autor no es un diccionario"
        
    if "nombre" not in post["autor"]:
        return False, "El diccionario autor no tiene la clave 'nombre'"
        
    if not isinstance(post["tags"], list):
        return False, "La clave 'tags' no es una lista"
        
    if post["estado"] not in estados_post:
        return False, f"Estado '{post['estado']}' no válido"
        
    return True, "Válido"