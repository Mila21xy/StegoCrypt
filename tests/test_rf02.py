from modules.image_lsb import (
    ocultar_mensaje,
    extraer_mensaje,
)


def ejecutar_prueba(nombre, imagen, mensaje, salida):

    print("=" * 60)
    print(nombre)
    print("=" * 60)

    ocultar_mensaje(
        imagen,
        mensaje,
        salida,
    )

    recuperado = extraer_mensaje(salida)

    print("Mensaje original:")
    print(mensaje)

    print()

    print("Mensaje recuperado:")
    print(recuperado)

    print()

    print("¿Coinciden?:", mensaje == recuperado)

    print()


def prueba_sin_mensaje():

    print("=" * 60)
    print("PRUEBA SIN MENSAJE")
    print("=" * 60)

    try:

        extraer_mensaje(
            "samples/images/prueba.png"
        )

    except Exception as e:

        print("✓ Error detectado correctamente")

        print(e)

    print()


def main():

    ejecutar_prueba(
        "PRUEBA PNG",
        "samples/images/prueba.png",
        "Hola Profesor",
        "output/rf02_png.png",
    )

    ejecutar_prueba(
        "PRUEBA BMP",
        "samples/images/prueba.bmp",
        "Universidad Ingeniería de Software",
        "output/rf02_bmp.bmp",
    )

    ejecutar_prueba(
        "PRUEBA MENSAJE LARGO",
        "samples/images/prueba.png",
        "Ciberseguridad " * 200,
        "output/rf02_largo.png",
    )

    ejecutar_prueba(
        "PRUEBA CARACTERES ESPECIALES",
        "samples/images/prueba.png",
        "1234567890 !?;.+,-_()[]{}",
        "output/rf02_especiales.png",
    )

    prueba_sin_mensaje()

    print("=" * 60)
    print("TODAS LAS PRUEBAS DEL RF02 FINALIZARON")
    print("=" * 60)


if __name__ == "__main__":
    main()