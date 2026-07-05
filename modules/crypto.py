"""
Módulo de cifrado utilizando Fernet.
"""

from pathlib import Path

from cryptography.fernet import Fernet


ARCHIVO_CLAVE = Path("data/key.key")


def generar_clave() -> bytes:
    """
    Genera una nueva clave y la guarda en disco.
    """

    clave = Fernet.generate_key()

    ARCHIVO_CLAVE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    ARCHIVO_CLAVE.write_bytes(clave)

    return clave


def cargar_clave() -> bytes:
    """
    Carga la clave existente.
    Si no existe, la genera automáticamente.
    """

    if not ARCHIVO_CLAVE.exists():
        return generar_clave()

    return ARCHIVO_CLAVE.read_bytes()


def obtener_fernet() -> Fernet:
    """
    Devuelve una instancia de Fernet.
    """

    return Fernet(cargar_clave())


def cifrar(mensaje: str) -> str:
    """
    Cifra un mensaje.
    """

    fernet = obtener_fernet()

    token = fernet.encrypt(
        mensaje.encode("utf-8")
    )

    return token.decode("utf-8")


def descifrar(token: str) -> str:
    """
    Descifra un mensaje.
    """

    fernet = obtener_fernet()

    mensaje = fernet.decrypt(
        token.encode("utf-8")
    )

    return mensaje.decode("utf-8")