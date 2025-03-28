# comandos.py: Contiene traducciones de comandos básicos y funciones matemáticas al español.

import math  # Necesario para funciones matemáticas avanzadas

# Comandos básicos


def imprimir(*args):
    """Función que traduce el comando print al español."""
    print(*args)


def entrada(mensaje):
    """Función que traduce el comando input al español."""
    return input(mensaje)


def longitud(objeto):
    """Función que traduce el comando len al español."""
    return len(objeto)


def tipo(objeto):
    """Función que traduce el comando type al español."""
    return type(objeto)

# Funciones matemáticas básicas


def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def resta(a, b):
    """Devuelve la resta de dos números."""
    return a - b


def multiplicacion(a, b):
    """Devuelve el producto de dos números."""
    return a * b


def division(a, b):
    """Devuelve el cociente de la división de dos números."""
    if b != 0:
        return a / b
    else:
        raise ValueError("El divisor no puede ser cero.")

# Funciones matemáticas avanzadas


def raiz_cuadrada(a):
    """Devuelve la raíz cuadrada de un número."""
    if a >= 0:
        return math.sqrt(a)
    else:
        raise ValueError(
            "No se puede calcular la raíz cuadrada de un número negativo.")


def potencia(base, exponente):
    """Devuelve la potencia de un número (base ^ exponente)."""
    return base ** exponente


def seno(angulo):
    """Devuelve el seno de un ángulo en radianes."""
    return math.sin(angulo)


def coseno(angulo):
    """Devuelve el coseno de un ángulo en radianes."""
    return math.cos(angulo)


def factorial(n):
    """Devuelve el factorial de un número entero no negativo."""
    if n >= 0 and isinstance(n, int):
        return math.factorial(n)
    else:
        raise ValueError(
            "El factorial solo está definido para enteros no negativos.")
