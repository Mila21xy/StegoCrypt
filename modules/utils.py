"""
Funciones compartidas del proyecto.
"""


def texto_a_bits(texto: str) -> str:
    """
    Convierte un texto a una cadena de bits.
    """
    return "".join(format(ord(c), "08b") for c in texto)


def bits_a_texto(bits: str) -> str:
    """
    Convierte una cadena de bits nuevamente a texto.
    """

    caracteres = []

    for i in range(0, len(bits), 8):

        byte = bits[i:i + 8]

        if len(byte) < 8:
            break

        caracteres.append(chr(int(byte, 2)))

    return "".join(caracteres)