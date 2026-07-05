from modules.image_lsb import *

print("=" * 50)
print("RF01 - Ocultación de mensajes en imágenes")
print("=" * 50)

mensaje = "Hola"

bits = texto_a_bits(mensaje)

print("Mensaje:", mensaje)
print("Bits:", bits)