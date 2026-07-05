"""
Módulo: image_lsb.py

Ocultación de mensajes de texto en imágenes PNG y BMP
utilizando la técnica Least Significant Bit (LSB).
"""

from PIL import Image
from modules.utils import texto_a_bits
from modules.utils import bits_a_texto
from modules.crypto import (
    cifrar as cifrar_texto,
    descifrar as descifrar_texto,
)
DELIMITADOR = "###END###"

FORMATOS_PERMITIDOS = (".png", ".bmp")


def validar_formato(ruta_imagen: str) -> None:
    """
    Verifica que la imagen tenga un formato permitido.
    """
    if not ruta_imagen.lower().endswith(FORMATOS_PERMITIDOS):
        raise ValueError("Solo se permiten imágenes PNG y BMP.")


def abrir_imagen(ruta_imagen: str) -> Image.Image:
    validar_formato(ruta_imagen)
    return Image.open(ruta_imagen).convert("RGB")


def obtener_bits_imagen(imagen: Image.Image) -> str:
    """
    Obtiene todos los bits LSB de la imagen.
    """

    bits = ""

    for r, g, b in imagen.getdata():

        bits += str(r & 1)
        bits += str(g & 1)
        bits += str(b & 1)

    return bits

def calcular_capacidad(imagen: Image.Image) -> int:
    """
    Calcula la capacidad máxima de caracteres.
    """

    ancho, alto = imagen.size

    bits = ancho * alto * 3

    return bits // 8


def validar_capacidad(imagen: Image.Image, mensaje: str) -> bool:

    capacidad = calcular_capacidad(imagen)

    return len(mensaje + DELIMITADOR) <= capacidad


def obtener_pixeles(imagen: Image.Image):

    return list(imagen.getdata())


def modificar_lsb(pixeles, bits):

    nuevos = []

    indice = 0

    for r, g, b in pixeles:

        rgb = [r, g, b]

        for i in range(3):

            if indice < len(bits):

                rgb[i] = (rgb[i] & 254) | int(bits[indice])

                indice += 1

        nuevos.append(tuple(rgb))

    return nuevos


def guardar_imagen(imagen: Image.Image, pixeles, ruta_salida: str):

    imagen.putdata(pixeles)

    imagen.save(ruta_salida)


def ocultar_mensaje(
    ruta_imagen: str,
    mensaje: str,
    ruta_salida: str,
    cifrar: bool = False,
):

    imagen = abrir_imagen(ruta_imagen)

    if not validar_capacidad(imagen, mensaje):
        raise ValueError(
            "La imagen no tiene suficiente capacidad."
        )    
    
    if cifrar:
        mensaje = cifrar_texto(mensaje)

    mensaje += DELIMITADOR

    bits = texto_a_bits(mensaje)

    pixeles = obtener_pixeles(imagen)

    nuevos = modificar_lsb(pixeles, bits)

    guardar_imagen(imagen, nuevos, ruta_salida)

def extraer_mensaje(
    ruta_imagen: str,
    descifrar: bool = False,
):
    """
    Extrae un mensaje oculto mediante LSB.
    """

    imagen = abrir_imagen(ruta_imagen)

    bits = obtener_bits_imagen(imagen)

    texto = bits_a_texto(bits)

    posicion = texto.find(DELIMITADOR)

    if posicion == -1:
        raise ValueError(
            "No se encontró un mensaje oculto."
        )


    mensaje = texto[:posicion]

    if descifrar:
        mensaje = descifrar_texto(mensaje)

    return mensaje