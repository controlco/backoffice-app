# Documentos de Pruebas

EL siguiente documento busca mostrar los resultados de los tests realizados a la aplicación, para asegurar el funcionamiento completo de la API.
En particular, se centró en la realización de Tests Unitarios a todos los endpoints de la API y verificaru su funcionamiento de acuerdo a lo esperado.

En particular, se realizaron tests a 8 modelos distintos, presentando un test unitario para cada endpoint utilizado en la API del modelo asociado.

El módulo utilizado fue APITestCase, proveniente de rest_framework.test
Este módulo nos presenta una adaptación para rest framework, de los tests unitarios implementados por python.

El código de los tests se puede encontrar el los archivos tests.py de las aplicaciones respectivas.

Se corren los tests con:

```
    docker-compose run web python manage.py test
```

Obteniendo los siguientes resultados:

```
System check identified no issues (0 silenced).
........
----------------------------------------------------------------------
Ran 8 tests in 5.271s

OK
```

En particular, la enumeración de tests se presenta a continuación:

- UserTests

  - sign_up
  - login
  - user_update

- ReportTests:

  - test_create_report

- MessageTests:

  - reate_message

- RegionTests:

  - create_region

- DistrictTests

  - create_district

- PropertyTests
  - create_property
