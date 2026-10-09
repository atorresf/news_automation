
from email.message import EmailMessage


def crear_correo(usuario: dict, noticia: dict) -> EmailMessage:
    """
    Construye un correo personalizado con una noticia.
    No realiza el envío.
    """

    nombre = usuario["nombre"]
    email = usuario["email"]
    categoria = usuario["categoria_favorita"]

    titulo = noticia.get("title", "Noticia de interés")
    descripcion = noticia.get("description") or ""
    enlace = noticia.get("url", "")

    asunto = f"Una buena noticia de {categoria} para ti"

    contenido = f"""Hola {nombre},

Encontramos una noticia que podría interesarte.

Categoría: {categoria}

{titulo}

{descripcion}

Puedes leer la noticia completa aquí:
{enlace}

¡Que tengas un excelente día!

Equipo de Noticias
"""

    mensaje = EmailMessage()
    mensaje["To"] = email
    mensaje["Subject"] = asunto
    mensaje.set_content(contenido)

    return mensaje


from pathlib import Path
from datetime import datetime


def simular_envio(mensaje):
    """
    Simula el envío de un correo electrónico.
    Guarda el mensaje en formato .eml.
    No envía correos reales.
    """

    # Crear carpeta de correos si no existe
    carpeta = Path("emails")
    carpeta.mkdir(exist_ok=True)

    # Crear un nombre único usando fecha y hora
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S_%f")

    archivo = carpeta / f"correo_{fecha}.eml"

    # Guardar el correo
    archivo.write_bytes(mensaje.as_bytes())

    print("\n========== ENVÍO  ==========")
    print(f"Destinatario: {mensaje['To']}")
    print(f"Asunto: {mensaje['Subject']}")
    #print("Estado: SIMULADO - NO ENVIADO")
    print(f"Archivo generado: {archivo.resolve()}")
    print("===================================")

    return archivo
