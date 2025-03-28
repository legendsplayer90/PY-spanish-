# operaciones.py: Contiene funciones matemáticas simples y avanzadas en español.

import math  # Usaremos esta biblioteca para funciones avanzadas

# Operaciones matemáticas simples


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

# Operaciones matemáticas avanzadas


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
