from modules.crypto import (
    generar_clave,
    cifrar,
    descifrar,
)

def prueba_dos_cifrados():

    print()
    print("=" * 60)
    print("PRUEBA DE CIFRADOS DIFERENTES")
    print("=" * 60)

    mensaje = "Hola Profesor"

    cifrado1 = cifrar(mensaje)
    cifrado2 = cifrar(mensaje)

    print("Cifrado 1:")
    print(cifrado1)

    print()

    print("Cifrado 2:")
    print(cifrado2)

    print()

    print("¿Son diferentes?:", cifrado1 != cifrado2)

def main():

    print("=" * 60)
    print("RF04 - Cifrado Fernet")
    print("=" * 60)

    generar_clave()

    mensaje = "Hola Profesor"

    print()

    print("Mensaje original:")
    print(mensaje)

    print()

    mensaje_cifrado = cifrar(mensaje)

    print("Mensaje cifrado:")
    print(mensaje_cifrado)

    print()

    mensaje_descifrado = descifrar(
        mensaje_cifrado
    )

    print("Mensaje recuperado:")
    print(mensaje_descifrado)

    print()

    print(
        "¿Coinciden?:",
        mensaje == mensaje_descifrado,
    )
    prueba_dos_cifrados()


if __name__ == "__main__":
    main()