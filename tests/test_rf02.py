from modules.image_lsb import (
    ocultar_mensaje,
    extraer_mensaje,
)


def main():

    print("=" * 60)
    print("RF02 - Extracción de mensajes")
    print("=" * 60)

    mensaje = (
        "Hola Profesor "
        "Este mensaje fue ocultado usando LSB."
    )

    ocultar_mensaje(
        "samples/images/prueba.png",
        mensaje,
        "output/rf02.png",
    )

    recuperado = extraer_mensaje(
        "output/rf02.png"
    )

    print()

    print("Mensaje original:")

    print(mensaje)

    print()

    print("Mensaje recuperado:")

    print(recuperado)

    print()

    print("¿Coinciden?:", mensaje == recuperado)

print()

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

if __name__ == "__main__":
    main()