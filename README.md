# News Automation — Noticias Positivas personalizadas

## Descripción

Aplicación desarrollada en Python que automatiza la selección de noticias personalizadas según las preferencias de un usuario.

El programa recibe un `user_id`, consulta dos archivos CSV, obtiene la categoría favorita del usuario, busca noticias recientes mediante GNews API y selecciona una noticia con indicadores de contenido positivo.

Finalmente, genera un correo personalizado en formato `.eml`, simulando su envío.

**Nota:** La versión actual no realiza envíos reales de correo electrónico.

## Tecnologías utilizadas

- Python 3.14
- pandas
- requests
- python-dotenv
- pytest
- GNews API

## Estructura del proyecto

```text
news_automation/
├── data/
│   ├── user_data_sample.csv
│   └── user_register_data_sample.csv
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── users.py
│   ├── news.py
│   └── email_service.py
├── tests/
│   ├── test_users.py
│   ├── test_news.py
│   └── test_email_service.py
├── emails/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

La carpeta `emails/` se crea automáticamente durante la ejecución y no se publica en el repositorio.

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone URL_DEL_REPOSITORIO
   cd news_automation
   ```

2. Crear un entorno virtual:

   ```bash
   python -m venv .venv
   ```

3. Activar el entorno virtual en Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Instalar las dependencias:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Crear un archivo `.env` basado en `.env.example`:

   ```dotenv
   GNEWS_API_KEY=TU_API_KEY
   ```

6. Colocar los archivos CSV requeridos en la carpeta `data/`.

## Ejecución

Desde la carpeta principal del proyecto:

```bash
python -m src.main
```

El programa solicitará un `user_id` válido.

A continuación:

1. Recupera los datos del usuario.
2. Obtiene su categoría favorita.
3. Consulta noticias mediante GNews.
4. Selecciona una noticia positiva candidata.
5. Construye un correo personalizado.
6. Guarda el mensaje en formato `.eml`.

## Pruebas automatizadas

Para ejecutar las pruebas:

```bash
python -m pytest -v
```

Se incluyen ocho pruebas para validar la búsqueda de usuarios, detección de duplicados, selección de noticias y personalización de correos.

## Seguridad

- Las claves API se almacenan en `.env`.
- `.env` no debe publicarse en GitHub.
- Los correos generados se excluyen mediante `.gitignore`.
- Los datos personales deben protegerse antes de publicar el repositorio.

## Limitaciones

- El envío de correo es simulado: no se utiliza SMTP ni un proveedor de envío real.
- La selección de noticias positivas utiliza palabras clave; no realiza un análisis semántico completo.
- La disponibilidad y cantidad de noticias dependen de GNews y de los límites de la API.
- Si no se encuentra una noticia positiva candidata, no se genera un correo.

## Posibles mejoras

- Integrar un proveedor de correo para realizar envíos reales.
- Implementar análisis de sentimiento más avanzado.
- Incorporar registros de ejecución y métricas.
- Agregar pruebas de integración y simulaciones de errores de la API.
