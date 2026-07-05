# StegoCrypt

Proyecto de Esteganografía en Imágenes y Audio desarrollado en Python.

## Funcionalidades

- Ocultación de mensajes en imágenes PNG/BMP mediante LSB.
- Extracción de mensajes ocultos.
- Ocultación de mensajes en archivos WAV.
- Cifrado AES (Fernet).
- Cálculo de capacidad máxima.
- Detección estadística mediante Chi-Square.
- Comparación de histogramas.
- Ocultación de archivos binarios.
- Registro de operaciones.
- Interfaz gráfica con PyQt5.

## Estructura del proyecto

- **assets/**: Recursos gráficos de la aplicación (iconos, imágenes de la interfaz, etc.).
- **data/**: Información utilizada por el programa.
  - **images/**: Imágenes de trabajo.
  - **audio/**: Audios de trabajo.
  - **logs/**: Registro de operaciones.
- **modules/**: Módulos principales del sistema.
- **samples/**: Archivos originales utilizados para las pruebas.
  - **images/**: Imágenes originales.
  - **audio/**: Audios originales.
- **output/**: Archivos generados por la aplicación (imágenes y audios con información oculta).
- **tests/**: Pruebas del proyecto.
- **ui/**: Interfaz gráfica desarrollada con PyQt5.

## Requerimiento Funcional 1

Estado: Completo

Funcionalidades implementadas:

- Conversión de texto a bits.
- Cálculo de capacidad de imágenes.
- Validación de capacidad.
- Validación de formatos PNG y BMP.
- Ocultación de mensajes mediante técnica LSB.
- Generación de imágenes con información oculta.

## Requerimiento Funcional 2

Estado: Completo

Funcionalidades implementadas

- Extracción de mensajes ocultos mediante LSB.
- Conversión de bits a texto.
- Lectura de bits desde imágenes.
- Validación de mensajes inexistentes.
- Compatibilidad con imágenes PNG.
- Compatibilidad con imágenes BMP.

## Requerimiento Funcional 3

Estado: Completo

Funcionalidades implementadas

- Ocultación de mensajes en archivos WAV.
- Extracción de mensajes desde archivos WAV.
- Validación de capacidad.
- Detección de audios sin mensaje.

## Requerimiento Funcional 4

Estado: Implementación del módulo de cifrado completa

Funcionalidades:

- Generación automática de clave.
- Almacenamiento seguro de la clave.
- Cifrado mediante Fernet (AES).
- Descifrado de mensajes.
- Pruebas unitarias del módulo.