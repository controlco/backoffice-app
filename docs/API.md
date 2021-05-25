# Documentación API

---

Index:

- [User](#user)

  - [POST signup/](#post-signup)
  - [POST login/](#post-login)
  - [GET, PATCH users/{user-id}/](#patch-userid)
  - [GET users/{user_id}/properties/](#get-usersproperty_idproperties)
  - [GET users/{user_id}/reports/](#get-usersreport_idreports)

- [Message](#message)

  - [GET users/{user_id}/messages/](#get-messages)
  - [GET users/{user_id}/messages/sent/](#get-messagessent)
  - [GET users/{user_id}/messages/received/](#get-messagesreceived)
  - [GET, PATCH users/{user_id}/messages/{message_id}/](#patch-messages)
  - [POST users/{user_id}/messages/](#post-messages)
  - [PATCH users/{user_id}/messages/{message_id}/read/](#patch-messagesread)

- [Region](#region)

  - [GET regions/](#get-regions)
  - [GET regions/{region_id}/districts/](#get-regionsdistrict_iddistricts)

- [District](#district)

  - [GET districts/](#get-districts)
  - [GET districts/{district_id}/properties/](#get-districtsproperty_idproperties)

- [Property](#property)

  - [GET properties/](#get-properties)
  - [POST properties/](#post-properties)
  - [GET, PATCH, DELETE properties/{id}/](#get-delete-propertiesid)

- [Report](#report)

  - [POST reports/](#post-properties)
  - [GET, PATCH, DELETE reports/{id}/](#get-delete-reportsid)

## [User](#documentación-api)

### POST signup/

- Registrarse. Notar que el atributo 'is_owner', toma valor true en aplicación web (propietarios), y false en mobile.

```
{
    "email": "new_user@gmail.com",
    "password": "123",
    "first_name": "Nombre",
    "last_name": "Apellido",
    "rut": "rut",
    "is_owner": true,
    "birth_date": "2019-02-03T06:48:07"
}
```

- Retorna:

```
{
    "success": "True",
    "status code": 201,
    "message": "User registered  successfully"
}
```

### POST login/

- Iniciar sesión:

```
{
    "email": "new_user@gmail.com",
    "password": "123"
}
```

- Retorna:

```
{
    "success": "True",
    "status code": 200,
    "message": "User logged in successfully",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo2LCJ1c2VybmFtZSI6Im5ld191c2VyQGdtYWlsLmNvbSIsImV4cCI6MTYyMzcyNzYzNSwiZW1haWwiOiJuZXdfdXNlckBnbWFpbC5jb20ifQ.jn2gWgcXEGYP3ppOqE3cvCK94kX--YKv5R8yAaYnbIE"
}
```

### GET users/{user_id}/

- Obtiene la información de un usuario:

```
{
    "id": 6,
    "email": "new_user@gmail.com",
    "first_name": "Nombre",
    "last_name": "Apellido",
    "rut": 111111,
    "birth_date": null,
    "is_owner": false,
    "is_active": true
}
```

### PATCH users/{user_id}/

- Actualiza la información del usuario. Si se actualiza el email, se debe hacer login nuevamente.

```
{
    "first_name": "Nombre Actualizado"
}
```

- Retorna:

```
{
    "id": 6,
    "email": "new_user@gmail.com",
    "first_name": "Nombre Actualizado",
    "last_name": "Apellido",
    "rut": 111111,
    "birth_date": null,
    "is_owner": false,
    "is_active": true
}
```

### GET users/{user_id}/reports/

- Entrega la lista de todas las denuncias realizadas por el usuario:

```
[
    {
        "title": "FUNA",
        "content": "ERA UNA ESTAFA",
        "owner": "user@uc.cl",
        "owner_id": 1,
        "reported_user": 2
    },
    {
        "title": "FUNA 2",
        "content": "ERA UNA ESTAFA",
        "owner": "user@uc.cl",
        "owner_id": 1,
        "reported_user": 3
    }
]
```

### GET users/{user_id}/properties/

- Entrega la lista de todas las propiedades publicadas por el usuario:

```
[
    {
        "id": 1,
        "title": "Bella casa con vista exclusiva",
        "owner_id": 2,
        "owner": "user2@uc.cl",
        "surface": 100,
        "adress": "Av Marco Marini 6622",
        "price": 1000000,
        "description": "Casa 5 estrellas",
        "latitude": "-22.9167",
        "longitude": "-68.2",
        "district": 1,
        "district_name": "Arica",
        "electricity_service": false,
        "water_service": false
    },
    {
        "id": 2,
        "title": "Casa en el cerro",
        "owner_id": 2,
        "owner": "user2@uc.cl",
        "surface": 20,
        "adress": "Av Pablo reyes 1231",
        "price": 100000,
        "description": "Buena vista al mar",
        "latitude": "-22.4167",
        "longitude": "-68.4",
        "district": 2,
        "district_name": "Camarones",
        "electricity_service": false,
        "water_service": false
    }
]
```

## [Message](#documentación-api)

### GET users/{user_id}/messages/

- Entrega la lista de todos los mensajes intercambiados por {user_id} y el usuario que envía la request:

```
[
    {
        "id": 1,
        "subject": "[Sin Asunto]",
        "content": "Hola!",
        "from_user_email": "user@uc.cl",
        "from_user_id": 1,
        "to_user_email": "user2@uc.cl",
        "to_user_id": 2,
        "read": false
    },
    {
        "id": 2,
        "subject": "[Sin Asunto]",
        "content": "Cómo estay?",
        "from_user_email": "user2@uc.cl",
        "from_user_id": 2,
        "to_user_email": "user@uc.cl",
        "to_user_id": 1,
        "read": false
    }
]
```

### GET users/{user_id}/messages/sent/

- Entrega la lista de todos los mensajes que {user_id} ha enviado:

```
[
    {
        "id": 1,
        "subject": "[Sin Asunto]",
        "content": "Hola!",
        "from_user_email": "user@uc.cl",
        "from_user_id": 1,
        "to_user_email": "user2@uc.cl",
        "to_user_id": 2,
        "read": false
    }
]
```

### GET users/{user_id}/messages/sent/

- Entrega la lista de todos los mensajes que {user_id} ha recibido:

```
[
    {
        "id": 2,
        "subject": "[Sin Asunto]",
        "content": "Cómo estay?",
        "from_user_email": "user2@uc.cl",
        "from_user_id": 2,
        "to_user_email": "user@uc.cl",
        "to_user_id": 1,
        "read": false
    }
]
```

### GET users/{user_id}/messages/{message_id}/

- Entrega los detalles del mensaje.
  No importa el valor de {user_id}, pues se podrá hacer la request solo si el mensaje le pertenece (o es el receptor) al usuario que realiza la request, por lo que si el {message_id} le pertenece, es válida:

```
{
    "id": 1,
    "subject": "[Sin Asunto]",
    "content": "Hola!",
    "from_user_email": "user@uc.cl",
    "from_user_id": 1,
    "to_user_email": "user2@uc.cl",
    "to_user_id": 2,
    "read": false
}
```

### PATCH users/{user_id}/messages/{message_id}/

- Actualiza los detalles del mensaje. No importa el valor de {user_id}, pues se podrá hacer la request solo si el mensaje le pertenece al usuario que realiza la request, por lo que si el {message_id} le pertenece, es válida:

```
{
    "subject": "Asunto actualizado",
    "content": "Hola!"
}
```

- Retorna:

```
{
    "id": 1,
    "subject": "Asunto actualizado",
    "content": "Hola!",
    "from_user_email": "user@uc.cl",
    "from_user_id": 1,
    "to_user_email": "user2@uc.cl",
    "to_user_id": 2,
    "read": false
}
```

### POST users/{user_id}/messages/

- Crea un nuevo mensaje. No importa el valor de {user_id}:

```
{
    "subject": "Asunto No vacío",
    "content": "Nuevo mensaje!",
    "to_user": 2
}
```

- Retorna:

```
{
    "id": 4,
    "subject": "Asunto No vacío",
    "content": "Nuevo mensaje!",
    "from_user_email": "user@uc.cl",
    "from_id": 1,
    "to_user_email": "user2@uc.cl",
    "to_user": 2,
    "read": false
}
```

### PATCH users/{user_id}/messages/{message_id}/read/

- Actualiza el valor del atribudo 'read' de un mensaje. No importa el valor de {user_id}:

```
{
    "read": true
}
```

- Retorna:

```
{
    "id": 1,
    "subject": "Saludo",
    "content": "Hola!",
    "from_user_email": "user@uc.cl",
    "from_id": 1,
    "to_user_email": "user2@uc.cl",
    "to_user": 2,
    "read": true
}
```

## [Region](#documentación-api)

### GET regions/

- Entrega la lista de todas las regiones (16):

```
[
    {
        "name": "Arica y Parinacota",
        "number": 15
    },
    {
        "name": "Tarapacá",
        "number": 1
    },
    {
        "name": "Antofagasta",
        "number": 2
    },
    {
        "name": "Atacama",
        "number": 3
    },
    {
        "name": "Coquimbo",
        "number": 4
    },
    {
        "name": "Valparaíso",
        "number": 5
    },
    {
        "name": "Metropolitana de Santiago",
        "number": 13
    },
    {
        "name": "Libertador Gral. Bernardo O’Higgins",
        "number": 6
    },
    {
        "name": "Maule",
        "number": 7
    },
    {
        "name": "Ñuble",
        "number": 16
    },
    {
        "name": "Biobío",
        "number": 8
    },
    {
        "name": "Araucanía",
        "number": 9
    },
    {
        "name": "Los Ríos",
        "number": 14
    },
    {
        "name": "Los Lagos",
        "number": 10
    },
    {
        "name": "Aisén del Gral. Carlos Ibáñez del Campo",
        "number": 11
    },
    {
        "name": "Magallanes y de la Antártica Chilena",
        "number": 12
    }
]
```

### GET regions/{region_id}/districts/

- Entrega la lista de todas las comunas de la región:

```
[
    {
        "name": "Alto Hospicio",
        "region": 1
    },
    {
        "name": "Camiña",
        "region": 1
    },
    {
        "name": "Colchane",
        "region": 1
    },
    {
        "name": "Huara",
        "region": 1
    },
    {
        "name": "Iquique",
        "region": 1
    },
    {
        "name": "Pica",
        "region": 1
    },
    {
        "name": "Pozo Almonte",
        "region": 1
    }
]
```

## [District](#documentación-api)

### GET districts/

- Entrega la lista de todas las comunas del país:

```
[
    {
        "name": "Arica",
        "region": 15
    },
    {
        "name": "Camarones",
        "region": 15
    },
    {
        "name": "General Lagos",
        "region": 15
    },
    {
        "name": "Putre",
        "region": 15
    },
    {
        "name": "Alto Hospicio",
        "region": 1
    },
    {
        "name": "Camiña",
        "region": 1
    },
    {
        "name": "Colchane",
        "region": 1
    }
]
```

### GET districts/{district_id}/properties/

- Entrega la lista de todas las propiedades de la comuna:

```
[
    {
        "id": 1,
        "title": "Bella casa con vista exclusiva",
        "owner": "user2@uc.cl",
        "owner_id": 2,
        "surface": 100,
        "adress": "Av Marco Marini 6622",
        "price": 1000000,
        "description": "Casa 5 estrellas",
        "latitude": "-22.9167",
        "longitude": "-68.2",
        "district": 1,
        "district_name": "Arica",
        "electricity_service": false,
        "water_service": false
    }
]
```

## [Property](#documentación-api)

### GET properties/

- Entrega la lista de todas las propiedades:

```
[
    {
        "id": 1,
        "title": "Bella casa con vista exclusiva",
        "owner": "user2@uc.cl",
        "owner_id": 2,
        "surface": 100,
        "adress": "Av Marco Marini 6622",
        "price": 1000000,
        "description": "Casa 5 estrellas",
        "latitude": "-22.9167",
        "longitude": "-68.2",
        "district": 1,
        "district_name": "Arica",
        "electricity_service": false,
        "water_service": false
    },
    {
        "id": 2,
        "title": "Casa en el cerro",
        "owner": "user2@uc.cl",
        "owner_id": 2,
        "surface": 20,
        "adress": "Av Pablo reyes 1231",
        "price": 100000,
        "description": "Buena vista al mar",
        "latitude": "-22.4167",
        "longitude": "-68.4",
        "district": 2,
        "district_name": "Camarones",
        "electricity_service": false,
        "water_service": false
    }
]
```

### POST properties/

- Crea una nueva propiedad asociada al usuario loggeado en la sesión:

```
{
          "title": "NUEVA",
          "surface": 20,
          "adress": "Av...",
          "district": 2
}
```

- Retorna:

```
{
    "title": "NUEVA",
    "owner": "ctcarstens@uc.cl",
    "surface": 20,
    "adress": "Av...",
    "price": null,
    "description": null,
    "latitude": null,
    "longitude": null,
    "electricity_service": false,
    "water_service": false
}
```

### PATCH properties/{property_id}/

- Actualiza la propiedad:

```
{
    "title": "NUEVA ACTUALIZADA",
    "surface": 20,
    "adress": "Av...",
    "price": null,
    "description": "NUEVA DESCRIPCIÓN",
    "latitude": null,
    "longitude": null
}
```

- Retorna:

```
{
    "title": "NUEVA ACTUALIZADA",
    "owner": "ctcarstens@uc.cl",
    "surface": 20,
    "adress": "Av...",
    "price": null,
    "description": "NUEVA DESCRIPCIÓN",
    "latitude": null,
    "longitude": null,
    "electricity_service": false,
    "water_service": false
}
```

### DELETE properties/{property_id}/

- Elimina la propiedad.
- Sin input ni respuesta.

## [Report](#documentación-api)

### POST reports/

- Crea una nueva denuncia asociada al usuario loggeado en la sesión, al denunciado reported_user:

```
{
    "title": "Estafa",
    "content": "Era una estafa",
    "reported_user": 2
}
```

- Retorna:

```
{
    "title": "Estafa",
    "content": "Era una estafa",
    "owner": "new_user@gmail.com",
    "owner_id": 6,
    "reported_user": 2
}
```

### GET reports/{report_id}

- Muestra una denuncia realizada:

```
{
    "title": "Estafa",
    "content": "Era una estafa",
    "owner": "new_user@gmail.com",
    "owner_id": 6,
    "reported_user": 2
}
```

### PATCH reports/{report_id}/

```
{
    "title": "Estafa Actualizada",
    "content": "Era una estafa",
    "owner": "new_user@gmail.com",
    "reported_user": 2
}
```

- Retorna:

```
{
    "title": "Estafa Actualizada",
    "content": "Era una estafa",
    "owner": "new_user@gmail.com",
    "owner_id": 6,
    "reported_user": 2
}
```
