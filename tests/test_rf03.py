from modules.audio_lsb import (
    abrir_audio,
    calcular_capacidad,
    validar_capacidad,
)


def main():

    print("=" * 60)
    print("RF03 - Audio WAV")
    print("=" * 60)

    audio = abrir_audio(
        "samples/audio/prueba.wav"
    )

    capacidad = calcular_capacidad(audio)

    print("Capacidad:")

    print(capacidad)

    mensaje = "Hola Profesor"

    print()

    print("¿Cabe?")

    print(
        validar_capacidad(
            audio,
            mensaje,
        )
    )


if __name__ == "__main__":
    main()