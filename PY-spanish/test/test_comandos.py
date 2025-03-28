import pytest
from py_spanish.comandos import imprimir, entrada, longitud


def test_imprimir(capsys):
    """Prueba la función imprimir."""
    imprimir("Hola Mundo")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hola Mundo"


def test_longitud():
    """Prueba la función longitud."""
    assert longitud([1, 2, 3]) == 3
    assert longitud("Python") == 6


def test_tipo():
    """Prueba la función tipo."""
