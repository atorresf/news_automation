
from pathlib import Path
import pandas as pd

# Carpeta principal del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

print("Archivo actual:", __file__)
print("Carpeta principal:", BASE_DIR)
print("Carpeta de datos:", DATA_DIR)


def obtener_usuario(user_id: str) -> dict:
    """
    Busca un usuario y sus preferencias usando user_id.
    Devuelve un diccionario con los datos encontrados.
    """

    archivo_usuarios = DATA_DIR / "user_data_sample.csv"
    archivo_preferencias = DATA_DIR / "user_register_data_sample.csv"

    # Leer archivos CSV
    usuarios = pd.read_csv(archivo_usuarios, dtype={"user_id": str})
    preferencias = pd.read_csv(archivo_preferencias, dtype={"user_id": str})

    # Relacionar ambos archivos mediante user_id
    datos = pd.merge(
        usuarios,
        preferencias,
        on="user_id",
        how="inner",
        validate="one_to_one"
    )

    # Buscar el identificador solicitado
    resultado = datos.loc[datos["user_id"] == user_id.strip()]

    if resultado.empty:
        raise ValueError(f"No se encontró el usuario: {user_id}")

    usuario = resultado.iloc[0]

    return {
        "user_id": str(usuario["user_id"]),
        "nombre": str(usuario["nombre"]),
        "apellido": str(usuario["apellido"]),
        "email": str(usuario["email"]),
        "pais": str(usuario["pais"]),
        "categoria_favorita": str(usuario["categoria_favorita"]),
        "recibe_promociones": bool(usuario["recibe_promociones"])
    }
