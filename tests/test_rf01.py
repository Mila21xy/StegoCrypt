from PIL import Image

from modules.image_lsb import (
    texto_a_bits,
    calcular_capacidad,
    validar_capacidad,
)


def probar_imagen(ruta):

    imagen = Image.open(ruta)

    capacidad = calcular_capacidad(imagen)

    print("-" * 50)
    print(ruta)
    print("Resolución:", imagen.size)
    print("Capacidad:", capacidad, "caracteres")

    mensaje = "Hola Mundo"

    print("Mensaje:", mensaje)

    print("Longitud:", len(mensaje))

    print("¿Cabe?:", validar_capacidad(imagen, mensaje))

    print()


def main():

    print("=" * 60)
    print("RF01 - Conversión y capacidad")
    print("=" * 60)

    texto = "Hola"

    print()

    print("Texto:", texto)

    print("Bits:")

    print(texto_a_bits(texto))

    print()

    probar_imagen("samples/images/prueba.png")

    probar_imagen("samples/images/prueba.bmp")


if __name__ == "__main__":
    main()