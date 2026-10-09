
import os
import requests
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

API_KEY = os.getenv("GNEWS_API_KEY")
BASE_URL = "https://gnews.io/api/v4/search"



def buscar_noticias(categoria: str) -> list:
    """
    Consulta noticias de una categoría en GNews.
    Maneja errores de conexión y de la API.
    """

    if not API_KEY:
        raise ValueError(
            "No se encontró GNEWS_API_KEY en el archivo .env"
        )

    if not categoria or not categoria.strip():
        raise ValueError("La categoría no puede estar vacía")

    parametros = {
        "q": categoria.strip(),
        "lang": "es",
        "max": 10,
        "sortby": "publishedAt",
        "apikey": API_KEY
    }

    try:
        respuesta = requests.get(
            BASE_URL,
            params=parametros,
            timeout=15
        )

        respuesta.raise_for_status()
        datos = respuesta.json()

        return datos.get("articles", [])

    except requests.exceptions.Timeout as error:
        raise RuntimeError(
            "La API de noticias tardó demasiado en responder"
        ) from error

    except requests.exceptions.HTTPError as error:
        codigo = error.response.status_code

        raise RuntimeError(
            f"GNews devolvió un error HTTP {codigo}"
        ) from error

    except requests.exceptions.RequestException as error:
        raise RuntimeError(
            "No fue posible conectarse con GNews"
        ) from error

    except ValueError as error:
        raise RuntimeError(
            "GNews devolvió una respuesta JSON inválida"
        ) from error




def seleccionar_noticia_positiva(noticias: list) -> dict | None:
    """
    Selecciona una noticia con indicadores positivos
    en su título o descripción.
    """

    palabras_positivas = [
        # Generales
        "avance", "logro", "éxito",
        "descubrimiento", "innovación",
        "mejora", "beneficio", "crecimiento",
        "récord", "premio", "solución", "progreso",

        # Deportes
        "victoria", "gana", "ganó",
        "campeón", "campeona", "campeonato",
        "medalla", "clasifica", "clasificó",
        "triunfo", "supera", "superó",

        # Ciencia y tecnología
        "desarrollo", "investigación",
        "cura", "tratamiento", "éxitoso"
    ]

    for noticia in noticias:
        titulo = noticia.get("title") or ""
        descripcion = noticia.get("description") or ""

        texto = f"{titulo} {descripcion}".lower()

        if any(palabra in texto for palabra in palabras_positivas):
            return noticia

    return None

