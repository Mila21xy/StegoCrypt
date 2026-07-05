from modules.image_lsb import (
    abrir_imagen,
    texto_a_bits,
    calcular_capacidad,
    validar_capacidad,
    ocultar_mensaje,
)


def prueba_conversion():

    print("=" * 60)
    print("PRUEBA 0 - Conversión de texto a bits")
    print("=" * 60)

    mensaje = "Hola"

    print("Mensaje:", mensaje)
    print("Bits:", texto_a_bits(mensaje))

    print()


def prueba_normal():

    print("=" * 60)
    print("PRUEBA 1 - Ocultación de mensaje")
    print("=" * 60)

    mensaje = "Hola Profesor"

    ocultar_mensaje(
        "samples/images/prueba.png",
        mensaje,
        "output/prueba_oculta.png",
    )

    print("✓ Mensaje ocultado correctamente")
    print("✓ Imagen generada en: output/prueba_oculta.png")

    print()


def prueba_capacidad():

    print("=" * 60)
    print("PRUEBA 2 - Capacidad de la imagen")
    print("=" * 60)

    imagen = abrir_imagen("samples/images/prueba.png")

    capacidad = calcular_capacidad(imagen)

    mensaje = "A" * (capacidad + 1)

    print("Capacidad:", capacidad)
    print("Longitud del mensaje:", len(mensaje))
    print("¿Cabe?:", validar_capacidad(imagen, mensaje))

    print()


def prueba_formato():

    print("=" * 60)
    print("PRUEBA 3 - Validación de formato")
    print("=" * 60)

    try:

        ocultar_mensaje(
            "README.md",
            "Hola",
            "output/test.png",
        )

    except Exception as e:

        print("✓ Error detectado correctamente")
        print("Mensaje:", e)

    print()


def main():

    print("\nRF01 - Ocultación de mensajes en imágenes mediante LSB\n")

    prueba_conversion()

    prueba_normal()

    prueba_capacidad()

    prueba_formato()

    print("=" * 60)
    print("TODAS LAS PRUEBAS DEL RF01 FINALIZARON")
    print("=" * 60)


if __name__ == "__main__":
    main()