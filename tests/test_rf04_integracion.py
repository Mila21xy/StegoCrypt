from modules.image_lsb import (
    ocultar_mensaje as ocultar_imagen,
    extraer_mensaje as extraer_imagen,
)

from modules.audio_lsb import (
    ocultar_mensaje as ocultar_audio,
    extraer_mensaje as extraer_audio,
)


def prueba_imagen():

    print("=" * 60)
    print("IMAGEN CIFRADA")
    print("=" * 60)

    mensaje = "Mensaje secreto para imagen"

    ocultar_imagen(
        "samples/images/prueba.png",
        mensaje,
        "output/imagen_cifrada.png",
        cifrar=True,
    )

    recuperado = extraer_imagen(
        "output/imagen_cifrada.png",
        descifrar=True,
    )

    print("¿Coinciden?:", mensaje == recuperado)
    print()


def prueba_audio():

    print("=" * 60)
    print("AUDIO CIFRADO")
    print("=" * 60)

    mensaje = "Mensaje secreto para audio"

    ocultar_audio(
        "samples/audio/prueba.wav",
        mensaje,
        "output/audio_cifrado.wav",
        cifrar=True,
    )

    recuperado = extraer_audio(
        "output/audio_cifrado.wav",
        descifrar=True,
    )

    print("¿Coinciden?:", mensaje == recuperado)
    print()


def main():

    prueba_imagen()
    prueba_audio()

    print("=" * 60)
    print("RF04 COMPLETADO")
    print("=" * 60)


if __name__ == "__main__":
    main()