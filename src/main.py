
from src.users import obtener_usuario
from src.news import buscar_noticias, seleccionar_noticia_positiva
from src.email_service import crear_correo, simular_envio


def main():
    user_id = input("Introduce el user_id: ").strip()

    try:
        # 1. Obtener información del usuario
        usuario = obtener_usuario(user_id)

        print(f"\nUsuario: {usuario['nombre']}")
        print(f"Categoría: {usuario['categoria_favorita']}")

        # 2. Consultar noticias
        noticias = buscar_noticias(
            usuario["categoria_favorita"]
        )

        print(f"Noticias encontradas: {len(noticias)}")

        # 3. Seleccionar una noticia positiva candidata
        noticia = seleccionar_noticia_positiva(noticias)

        if noticia is None:
            print("No se encontró una noticia positiva candidata.")
            return

        print(f"Noticia seleccionada: {noticia['title']}")

        # 4. Construir el correo
        mensaje = crear_correo(usuario, noticia)

        # 5. Simular el envío
        simular_envio(mensaje)

        print("\nProceso finalizado correctamente.")

    except Exception as error:
        print(f"\nError durante el proceso: {error}")


if __name__ == "__main__":
    main()
