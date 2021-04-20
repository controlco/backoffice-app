# Django API

Backend para la Administración de Propiedades.

## Requisitos

- python 3.6+
- pip/pip3
- virtualenv
- postgresql 12+

## Setup Mínimo

1. Clonar el repositorio localmente
2. [Instalar y preparar un entorno virtual](#entorno-virtual) en la carpeta raíz (donde se encuentra el archivo `requirements.txt`).
3. Instalar **postgresql 12** y [crear una base de datos para utilizar localmente](#base-de-datos) (https://www.postgresql.org/download/).
4. Crear un archivo `.env` en el directorio `app/app/` (donde se encuentra el módulo `settings.py`) y [setear las variables de entorno](#variables-de-entorno).
5. Correr `docker-compose up`.
6. Correr `docker-compose run web python manage.py migrate`.

## Entorno Virtual

A continuación se muestran los pasos para instalar y preparar un entorno virtual con `virtualenv`:

1. Instalar la librería: `pip3 install virtualenv`.
2. En la misma carpeta que el archivo `requirements.txt`, correr el comando: `virtualenv venv`.
3. A continuación correr `source venv/bin/activate` **(Linux/MacOS)** o `source venv/Scripts/activate` **(Windows)** para activar el entorno virtual.
4. Para instalar todas las dependencias en el entorno automáticamente, se debe correr el siguiente comando: `pip install -r requirements.txt` (en la carpeta donde está el archivo `requirements.txt`).
5. Si se instalan nuevas librerías en el entorno virtual, se deben guardar en el archivo `requirements.txt` mediante el siguiente comando: `pip freeze > requirements.txt`.
6. Para salir del entorno virtual se usa `deactivate`. **IMPORTANTE: Los pasos 4-5 deben siempre ser ejecutados con el entorno virtual activado.**

## Base de Datos

A continuación se muestran los pasos para preparar la base de datos:

1. Teniendo **postgresql 12** instalado, ingresar a su consola con el comando: `psql` (debe estar corriendo el servicio de postgresql).
2. Crear una base de datos nueva con el comando `CREATE DATABASE dbname;`.
3. Recordar el **nombre** de esta nueva base de datos recién creada, además del **usuario** y **contraseña** que se usaron para entrar a la consola de postgresql.

## Variables de Entorno Docker-compose

Para setear las variables de entorno de DOCKER-COMPOSE se debe crear un archivo `postgres-variables.env` en la root (donde se encuentra el archivo docker-compose.yml):

```
POSTGRES_DB=****             # El nombre de la base de datos creada en la sección 'Base de Datos'
POSTGRES_USER=****             # El usuario de postgresql creado
POSTGRES_PASSWORD=****         # La contraseña de postgresql creada
POSTGRES_HOST=db        # El dominio donde se encuentra la base de datos
POSTGRES_PORT=5432             # El puerto donde está corriendo la base de datos (por default es el 5432)
```

## Variables de Entorno Django

Para setear las variables de entorno DE DJANGO se debe crear un archivo `.env` a la misma altura del archivo setting.py con el siguiente formato:

```
ENV=development
POSTGRES_DB=****             # El nombre de la base de datos creada en la sección 'Base de Datos'
POSTGRES_USER=****             # El usuario de postgresql creado
POSTGRES_PASSWORD=****         # La contraseña de postgresql creada
POSTGRES_HOST=db        # El dominio donde se encuentra la base de datos
POSTGRES_PORT=5432             # El puerto donde está corriendo la base de datos (por default es el 5432)
```
