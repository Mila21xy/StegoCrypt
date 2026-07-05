"""
Módulo para ocultar mensajes en archivos WAV utilizando LSB.
"""

import wave

from modules.utils import (
    texto_a_bits,
    bits_a_texto,
)

DELIMITADOR = "###END###"


def abrir_audio(ruta_audio: str):
    return wave.open(ruta_audio, "rb")


def calcular_capacidad(audio) -> int:
    return audio.getnframes() // 8


def validar_capacidad(audio, mensaje: str) -> bool:
    return len(mensaje + DELIMITADOR) <= calcular_capacidad(audio)


def ocultar_mensaje(
    ruta_audio: str,
    mensaje: str,
    ruta_salida: str,
) -> None:

    audio = wave.open(ruta_audio, "rb")

    if not validar_capacidad(audio, mensaje):
        raise ValueError(
            "El audio no tiene suficiente capacidad."
        )

    parametros = audio.getparams()

    frames = bytearray(audio.readframes(audio.getnframes()))

    mensaje += DELIMITADOR

    bits = texto_a_bits(mensaje)

    for i, bit in enumerate(bits):

        frames[i] = (frames[i] & 254) | int(bit)

    salida = wave.open(ruta_salida, "wb")

    salida.setparams(parametros)

    salida.writeframes(frames)

    salida.close()

    audio.close()


def extraer_mensaje(
    ruta_audio: str,
) -> str:

    audio = wave.open(ruta_audio, "rb")

    frames = bytearray(audio.readframes(audio.getnframes()))

    bits = ""

    for byte in frames:

        bits += str(byte & 1)

    texto = bits_a_texto(bits)

    audio.close()

    posicion = texto.find(DELIMITADOR)

    if posicion == -1:

        raise ValueError(
            "No se encontró un mensaje oculto."
        )

    return texto[:posicion]