from modules.audio_lsb import (
    ocultar_mensaje,
    extraer_mensaje,
)


def ejecutar_prueba():

    mensaje = (
        "Hola Profesor "
        "este audio utiliza esteganografia LSB."
    )

    ocultar_mensaje(
        "samples/audio/prueba.wav",
        mensaje,
        "output/audio_oculto.wav",
    )

    recuperado = extraer_mensaje(
        "output/audio_oculto.wav"
    )

    print("=" * 60)

    print("Mensaje original:")

    print(mensaje)

    print()

    print("Mensaje recuperado:")

    print(recuperado)

    print()

    print("¿Coinciden?:", mensaje == recuperado)

    print("=" * 60)


def prueba_sin_mensaje():

    print()

    print("=" * 60)

    print("PRUEBA SIN MENSAJE")

    print("=" * 60)

    try:

        extraer_mensaje(
            "samples/audio/prueba.wav"
        )

    except Exception as e:

        print("✓ Error detectado correctamente")

        print(e)


def main():

    ejecutar_prueba()

    prueba_sin_mensaje()


if __name__ == "__main__":
    main()