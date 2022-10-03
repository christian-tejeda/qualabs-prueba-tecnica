### Prueba técnica - Qualabs

#### Parte A

```sh
pip install natsort
python providers.py
```

Genera el archivo `providers.json`, que para cada módulo contiene una lista con los usuarios que lo utilizan, separado por proveedor (content_module y auth_module).

#### Parte B

```sh
python users.py
```

Devuelve en la terminal una lista de usuarios que satisface la condición; los usuarios que aparecen utilizan todos los módulos disponibles.

Probado sobre Python 3.8.10 64-bit