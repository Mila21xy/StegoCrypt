from PIL import Image

from modules.image_lsb import (
    texto_a_bits,
    calcular_capacidad,
    validar_capacidad,
    ocultar_mensaje,
)


def prueba_normal():

    print("=" * 60)
    print("PRUEBA 1")
    print("=" * 60)

    mensaje = "Hola Profesor"

    ocultar_mensaje(
        "samples/images/prueba.png",
        mensaje,
        "output/prueba_oculta.png",
    )

    print("✓ Mensaje ocultado correctamente")


def prueba_capacidad():

    print("=" * 60)
    print("PRUEBA 2")
    print("=" * 60)

    imagen = Image.open("samples/images/prueba.png")

    capacidad = calcular_capacidad(imagen)

    mensaje = "A" * (capacidad + 1)

    print("Capacidad:", capacidad)

    print("Mensaje:", len(mensaje))

    print("¿Cabe?:", validar_capacidad(imagen, mensaje))


def prueba_formato():

    print("=" * 60)
    print("PRUEBA 3")
    print("=" * 60)

    try:

        ocultar_mensaje(
            "README.md",
            "Hola",
            "output/test.png",
        )

    except Exception as e:

        print("✓ Error detectado correctamente")

        print(e)


def main():

    prueba_normal()

    print()

    prueba_capacidad()

    print()

    prueba_formato()


if __name__ == "__main__":
    main()