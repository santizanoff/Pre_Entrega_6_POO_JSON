class Autor:
    def __init__(self, nombre, bio):
        self.nombre = nombre
        self.bio = bio

    # Serialización: Convierte el objeto a un formato compatible con JSON
    def to_dict(self):
        return {"nombre": self.nombre, "bio": self.bio}

    # Deserialización: Crea una instancia desde un diccionario leído del JSON
    @classmethod
    def from_dict(cls, data):
        return cls(data["nombre"], data["bio"])


class Post:
    def __init__(self, id_post, titulo, contenido, autor, tags, estado="Borrador"):
        self.id = id_post
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor  # Esto recibirá una instancia completa de la clase Autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),  # Ejecuta la serialización de la clase anidada
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, data):
        autor = Autor.from_dict(data["autor"])  # Reconstruye el objeto Autor primero
        return cls(data["id"], data["titulo"], data["contenido"], autor, data["tags"], data["estado"])


class Blog:
    def __init__(self):
        self.posts = []  # Centraliza el almacenamiento en memoria

    def agregar_post(self, post):
        self.posts.append(post)

    def listar_posts(self):
        return self.posts

    def buscar_por_titulo(self, titulo):
        return [p for p in self.posts if titulo.lower() in p.titulo.lower()]

    def filtrar_por_tag(self, tag):
        return [p for p in self.posts if tag.lower() in [t.lower() for t in p.tags]]