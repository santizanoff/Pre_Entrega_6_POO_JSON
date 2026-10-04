## Pre_Entrega_6_POO_JSON

## Arquitectura del Sistema: Modelado Orientado a Objetos y Persistencia JSON

### 1. Componentes Principales
* **Modelado de Dominio (`blog/modelos.py`):** Estructura formal basada en clases (`Autor`, `Post`, `Blog`). Se establece una relación de composición donde cada objeto `Post` contiene y administra una instancia dedicada de la clase `Autor`.
* **Motor de Reglas y Lógica:** La clase `Blog` asume la responsabilidad de centralizar la colección de registros en memoria y encapsula las operaciones analíticas del sistema: búsquedas insensibles a mayúsculas y minúsculas, filtrado vectorial por etiquetas (tags) y agregación de publicaciones.
* **Persistencia y Serialización (`blog/datos.py` & `posts.json`):** Implementación de una capa de entrada/salida que maneja métodos bidireccionales (`to_dict` y `from_dict`). Esto garantiza la transformación controlada de objetos en estructuras clave-valor serializables en formato JSON y viceversa, permitiendo la persistencia íntegra del estado entre ejecuciones.
* **Pipeline de Ingesta y Limpieza Inicial (`migrar_datos.py`):** Script desacoplado de ETL (Extract, Transform, Load) diseñado para procesar colecciones crudas preexistentes. Realiza la normalización de entidades mixtas (autores escalares vs. estructurados), imputa valores faltantes en campos críticos (`titulo`, `tags`) e hidrata los objetos de dominio para generar el estado base reproducible en `posts.json`.
* **Controlador de Flujo (`main.py`):** Desacoplamiento total entre la interfaz por consola (CLI) y la persistencia de datos. El script principal orquesta la carga inicial hacia una instancia de `Blog`, delega las operaciones a los métodos de la clase y administra el guardado en disco protegido bajo la condición `if __name__ == "__main__":`.

### 2. Fundamentos Técnicos y Criterios de Diseño
* **Contratos de Datos y Tipado Predecible:** La encapsulación de entidades elimina los errores por acceso a claves arbitrarias comunes en diccionarios anidados, asegurando que cada atributo (`titulo`, `autor`, `tags`) posea validación consistente en todo el ciclo de ejecución.
* **Separación de Responsabilidades (SoC):** La arquitectura aísla la capa de presentación (`menu.py`/`main.py`), la capa analítica y lógica (`modelos.py`), los procesos batch de ingesta (`migrar_datos.py`) y la capa de almacenamiento (`datos.py`), garantizando un mantenimiento modular y preparando el código para futuras transiciones hacia frameworks web o bases de datos estructuradas.
* **Tolerancia a Fallos e Integridad I/O:** El subsistema de persistencia aísla excepciones típicas de lectura/escritura (ausencia de archivo, JSON mal formado o esquemas incompletos), asegurando que el flujo interactivo no interrumpa su ejecución ante datos corruptos.
