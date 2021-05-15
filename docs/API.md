# Documentación API

---

Index:

- [User](#region)

  ... Completar Javi y Jose ...

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

### GET users/{user_id}/reports/

- Entrega la lista de todas las denuncias realizadas por el usuario:

```
[
    {
        "title": "Estafa 1",
        "content": "Era una estafa",
        "owner": 1,
        "reported_user": 2
    },
    {
        "title": "Estafa 2",
        "content": "Era una estafa",
        "owner": 1,
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
        "title": "Bella casa",
        "owner": "ct@uc.cl",
        "surface": 10,
        "adress": "Av...",
        "price": null,
        "description": null,
        "latitude": null,
        "longitude": null,
        "district": 1,
        "district_name": "Arica"
    }
]
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
    },
]
```

### GET districts/{district_id}/properties/

- Entrega la lista de todas las propiedades de la comuna:

```
[
    {
        "title": "Bella casa",
        "owner": "ctcarstens@uc.cl",
        "surface": 10,
        "adress": "Av...",
        "price": null,
        "description": null,
        "latitude": null,
        "longitude": null
    }
]
```

## [Property](#documentación-api)

### GET properties/

- Entrega la lista de todas las propiedades:

```
[
    {
        "title": "Bella casa",
        "owner": "ctcarstens@uc.cl",
        "surface": 10,
        "adress": "Av...",
        "price": null,
        "description": null,
        "latitude": null,
        "longitude": null
    },
    {
        "title": "Fea casa",
        "owner": "ctcarstens2@uc.cl",
        "surface": 20,
        "adress": "Av...",
        "price": null,
        "description": null,
        "latitude": null,
        "longitude": null
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
    "longitude": null
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
    "longitude": null
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
    "owner": 1,
    "reported_user": 2
}
```

- Retorna:

```
{
    "title": "Estafa",
    "content": "Era una estafa",
    "owner": 1,
    "reported_user": 2
}
```

### GET reports/{report_id}

- Muestra una denuncia realizada:

```
{
    "title": "Estafa",
    "content": "Era una estafa",
    "owner": 1,
    "reported_user": 2
}
```

### PATCH reports/{report_id}/

```
{
    "title": "Estafa NUEVA",
    "content": "Era una estafa",
    "owner": 1,
    "reported_user": 2
}
```

- Retorna:

```
{
    "title": "Estafa NUEVA",
    "content": "Era una estafa",
    "owner": 1,
    "reported_user": 2
}
```
