"""
Módulo: image_lsb.py

Implementa funciones para ocultar mensajes en imágenes
utilizando la técnica LSB.
"""

from PIL import Image


def texto_a_bits(texto: str) -> str:
    """
    Convierte un texto en una cadena de bits.
    """
    return "".join(format(ord(c), "08b") for c in texto)


def calcular_capacidad(imagen: Image.Image) -> int:
    """
    Calcula la cantidad máxima de caracteres que pueden ocultarse.

    Se utiliza 1 bit por canal RGB.

    3 bits por píxel.
    8 bits por carácter.
    """

    ancho, alto = imagen.size

    pixeles = ancho * alto

    bits_disponibles = pixeles * 3

    caracteres = bits_disponibles // 8

    return caracteres


def validar_capacidad(imagen: Image.Image, mensaje: str) -> bool:
    """
    Verifica si el mensaje cabe dentro de la imagen.
    """

    capacidad = calcular_capacidad(imagen)

    return len(mensaje) <= capacidad


def ocultar_mensaje(
    ruta_imagen: str,
    mensaje: str,
    ruta_salida: str,
):
    """
    Se implementará en el siguiente bloque.
    """
    pass