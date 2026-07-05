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