# Construcción de la lista de usuarios de cobertura mínima:
# Se buscan los usuarios con más coincidencias sobre el conjunto de proveedores
# Aquellos con más coincidencias se agregan a la solución; los conjuntos cubiertos se eliminan de los restantes
# Se devuelve la lista cuando ya no quedan proveedores por cubrir.

import os, json, natsort as ns

json_folder = './json/'
json_list = []
users = ns.natsorted(os.listdir(json_folder))

for user in users:
    try:
        file = open(json_folder + user)
    except:
        print('Ocurrió un error al cargar el archivo. Tal vez no exista o no tienes los permisos necesarios.')
    data = json.load(file)
    json_list.append(data)
    file.close()

module_group = set()

for item in json_list:
    module_group.add(item['provider']['auth_module'])
    module_group.add(item['provider']['content_module'])

min_user_list = []

while (len(module_group) > 0):
    i = 0
    best_current = {
        'user': '',
        'auth_module': '',
        'content_module': '',
        'hits': 0
    }
    for item in json_list:
        hits = 0
        if item['provider']['auth_module'] in module_group:
            hits += 1
        if item['provider']['content_module'] in module_group:
            hits += 1
        if (hits > best_current['hits']):
            best_current = {
                'user': users[i],
                'auth_module': item['provider']['auth_module'],
                'content_module': item['provider']['content_module'],
                'hits': hits
            }
        i += 1
    module_group.remove(best_current['auth_module'])
    module_group.remove(best_current['content_module'])
    min_user_list.append(best_current['user'])

print(min_user_list)