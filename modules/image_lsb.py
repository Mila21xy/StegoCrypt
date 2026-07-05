"""
Módulo: image_lsb.py

Ocultación de mensajes de texto en imágenes PNG y BMP
utilizando la técnica Least Significant Bit (LSB).
"""

from PIL import Image

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


def texto_a_bits(texto: str) -> str:
    """
    Convierte un texto a una cadena de bits.
    """
    return "".join(format(ord(c), "08b") for c in texto)


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
):

    imagen = abrir_imagen(ruta_imagen)

    validar_capacidad(imagen, mensaje)

    mensaje += DELIMITADOR

    bits = texto_a_bits(mensaje)

    pixeles = obtener_pixeles(imagen)

    nuevos = modificar_lsb(pixeles, bits)

    guardar_imagen(imagen, nuevos, ruta_salida)