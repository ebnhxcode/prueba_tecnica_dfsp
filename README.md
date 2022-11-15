# Prueba Técnica Desarrollador Full Stack (Backend)

Aplicación/API que actuará como intermediario en el consumo de servicios interoperando con la api datos gob.

## Requisitos

Los aspectos considerados son:
- [x] Desarrollo de api para la resolución de la prueba técnica.

Tecnologías usadas en el desarrollo de la api:
- [x] Docker.
- [x] Docker compose.
- [x] Python.
- [x] Flask, Flask RestX.
- [x] Entorno de desarrollo Unix (Recomendado), aunque también se puede en Wsl2 de windows.
- [x] Variables de entorno entregadas a continuación.


## Variables de Entorno


```
APP_NAME="api_datos_gob"
APP_TITLE="API DATOS GOB"
APP_DESCRIPTION="API para consumo de Servicio de Datos de Gobierno Digital."
APP_VERSION="1.0.0"
APP_URL_PREFIX="/api/v1"
APP_URL="http://localhost"
APP_HOST="0.0.0.0"
APP_PORT=5555
DEBUG=True
THREADED=True
TZ="America/Santiago"
TIMEZONE="America/Santiago"
FALLBACK_TIMEZONE="UTC"
LOCALE="America/Santiago"
FALLBACK_LOCALE="UTC"
LOG_PATH="/main/storage/logs"

PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1
PYTHONWARNINGS="ignore:Unverified HTTPS request" 

FLASK_APP=app.py
FLASK_SECRET_KEY=tokenaleatoriodigitalgobcl
SECRET_KEY=tokenaleatoriodigitalgobcl
FLASK_DEBUG=1
FLASK_ENV=development
ENV_FLASK=development

API_ENDPOINT="https://datos.gob.cl/dataset/33355/resource/3d54e961-d81b-4507-aeee-7a433e00a9bf"
API_ENDPOINT_QUERY="https://datos.gob.cl/api/3/action/datastore_search?resource_id=3d54e961-d81b-4507-aeee-7a433e00a9bf"
VALIDTOKENS=validtoken,token1,token2,token3
X_API_KEY=validtoken
AUTH_USERNAME=APIDATOSGOB
AUTH_PASSWORD=tokenaleatoriogobdigitalcl
```

## Instalación

Consideraciones específicas previas:
Al utilizar el archivo docker-compose de este proyecto, se requerirá que se cree una red local aislada para la api, esto se realiza como practica para aislar aplicaciones locales y usar aliases para llegar a endpoints. Podemos resolverlo ejecutando:
```
docker network create localnet
```

### Construcción de la imagen usando docker compose en un entorno de desarrollo local (Recomendado)

Ingresar al repositorio descargado, construir la imagen y levantar la app con docker-compose. Ejecutamos:
```
cd repo
docker-compose up --build api
```
