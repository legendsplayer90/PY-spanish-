# PY-spanish
"PY-spanish" es una librería que traduce y simplifica el uso de Python al español. Ofrece comandos básicos y funciones matemáticas en español para facilitar el aprendizaje y la programación.

## Instalación
Puedes instalar la librería directamente desde PyPI (cuando esté publicada):
pip install PY-spanish


O, si deseas probarla localmente, clona el repositorio y usa:
pip install .

## Uso
Aquí tienes ejemplos de cómo usar "PY-spanish":

### Comandos básicos
```python
from py_spanish import imprimir, entrada, longitud, tipo

imprimir("¡Hola, mundo!")  # Traducción de print
nombre = entrada("¿Cómo te llamas? ")  # Traducción de input
imprimir("Tu nombre tiene", longitud(nombre), "caracteres.")
imprimir("El tipo de tu entrada es:", tipo(nombre))
