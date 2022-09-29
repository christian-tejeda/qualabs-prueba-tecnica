import os, json

try:
    file = open('providers.json')
except:
    print('Ocurrió un error al cargar el archivo. Tal vez no exista o no tienes los permisos necesarios.')