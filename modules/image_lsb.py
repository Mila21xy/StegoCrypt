"""
Módulo: image_lsb.py

Implementa las funciones necesarias para ocultar mensajes
en imágenes PNG y BMP utilizando la técnica LSB
(Least Significant Bit).
"""

from PIL import Image


def texto_a_bits(texto):
    """
    Convierte un texto en una cadena de bits.
    """

    bits = ""

    for caracter in texto:
        bits += format(ord(caracter), "08b")

    return bits


def calcular_capacidad(imagen):
    """
    Calcula cuántos caracteres pueden ocultarse.
    """
    pass


def ocultar_mensaje(ruta_imagen, mensaje, ruta_salida):
    """
    Oculta un mensaje dentro de una imagen.
    """
    pass