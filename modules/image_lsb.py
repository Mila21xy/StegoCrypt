"""
Módulo: image_lsb.py

Implementa funciones para ocultar mensajes
en imágenes utilizando la técnica LSB.
"""

from PIL import Image

DELIMITADOR = "###END###"


def texto_a_bits(texto: str) -> str:
    return "".join(format(ord(c), "08b") for c in texto)


def calcular_capacidad(imagen: Image.Image) -> int:
    ancho, alto = imagen.size
    return (ancho * alto * 3) // 8


def validar_capacidad(imagen: Image.Image, mensaje: str) -> bool:
    return len(mensaje + DELIMITADOR) <= calcular_capacidad(imagen)


def ocultar_mensaje(
    ruta_imagen: str,
    mensaje: str,
    ruta_salida: str,
) -> None:

    imagen = Image.open(ruta_imagen).convert("RGB")

    if not validar_capacidad(imagen, mensaje):
        raise ValueError("La imagen no tiene suficiente capacidad.")

    mensaje += DELIMITADOR

    bits = texto_a_bits(mensaje)

    indice = 0

    pixeles = list(imagen.getdata())

    nuevos_pixeles = []

    for r, g, b in pixeles:

        rgb = [r, g, b]

        for i in range(3):

            if indice < len(bits):

                rgb[i] = (rgb[i] & 0b11111110) | int(bits[indice])

                indice += 1

        nuevos_pixeles.append(tuple(rgb))

    imagen.putdata(nuevos_pixeles)

    imagen.save(ruta_salida)