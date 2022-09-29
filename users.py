import os, json

json_folder = './json/'
json_result = 'providers.json'

json_list = []
users = sorted(os.listdir(json_folder))
providers = {
    'auth_module': {
    },
    'content_module': {
    }
}

for user in users:
    try:
        file = open(json_folder + user)
    except:
        print('Ocurrió un error al cargar el archivo. Tal vez no exista o no tienes los permisos necesarios.')
    data = json.load(file)
    json_list.append(data)
    file.close()

for item in json_list:
    current_auth_provider = item['provider']['auth_module']
    current_content_provider = item['provider']['content_module']
    providers['auth_module'][current_auth_provider] = []
    providers['content_module'][current_content_provider] = []


i = 0
for item in json_list:
    current_user_file = users[i]
    current_auth_provider = item['provider']['auth_module']
    current_content_provider = item['provider']['content_module']
    if (current_auth_provider == item['provider']['auth_module']):
        providers['auth_module'][current_auth_provider].append('./' + current_user_file)
    if (current_content_provider == item['provider']['content_module']):
        providers['content_module'][current_content_provider].append('./' + current_user_file)
    i += 1

with open(json_result, 'w') as file:
    try:
        json_str = json.dumps(providers, indent=2)
        file.write(json_str)
    except:
        print('Ocurrió un error al guardar el resultado.')