from PIL import Image

from modules.image_lsb import (
    texto_a_bits,
    calcular_capacidad,
    validar_capacidad,
    ocultar_mensaje,
)


def mostrar_info(ruta):

    imagen = Image.open(ruta)

    print("-" * 50)

    print("Imagen:", ruta)

    print("Resolución:", imagen.size)

    print("Capacidad:", calcular_capacidad(imagen))

    print()


def main():

    print("=" * 60)
    print("RF01 - Ocultación de mensajes")
    print("=" * 60)

    mensaje = "Hola Profesor"

    print()

    print("Mensaje:")

    print(mensaje)

    print()

    print("Bits:")

    print(texto_a_bits(mensaje))

    print()

    mostrar_info("samples/images/prueba.png")

    ocultar_mensaje(
        "samples/images/prueba.png",
        mensaje,
        "output/prueba_oculta.png",
    )

    print("Imagen generada correctamente.")

    print()

    mostrar_info("output/prueba_oculta.png")


if __name__ == "__main__":
    main()