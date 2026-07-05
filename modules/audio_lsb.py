"""
Módulo para ocultar mensajes
en archivos WAV usando LSB.
"""

import wave

from modules.utils import (
    texto_a_bits,
    bits_a_texto,
)

DELIMITADOR = "###END###"


def abrir_audio(ruta):

    return wave.open(ruta, "rb")


def calcular_capacidad(audio):

    frames = audio.getnframes()

    return frames // 8


def validar_capacidad(audio, mensaje):

    return len(mensaje + DELIMITADOR) <= calcular_capacidad(audio)


def ocultar_mensaje(
    ruta_audio,
    mensaje,
    ruta_salida,
):
    """
    Se implementará
    en el siguiente bloque.
    """
    pass


def extraer_mensaje(ruta_audio):
    """
    Se implementará
    en el siguiente bloque.
    """
    pass