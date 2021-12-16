'''Consulta datos en la Api de github y los ordena por los que tienen más estrellas'''

# El Requests permite a un programa de Python solicitar información a un sitio web y
# examinar la respuesta.
import requests

# Hace una llamada al Api de GitHub y guarda la respuesta.
# Github va por la tercera versión del api asi que usamos esa.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

# Usamos request para hacer la llamada al API. Usamos get() y le pasamos la url
# y el encabezado que hemos definido y asignamos el objeto de respuesta a al variable r.
r = requests.get(url, headers=headers)

# Este objeto tiene un atributo llamado status_code que nos indica una respuesta exitosa
# si el valor es 200
print(f"Status code: {r.status_code}")

# Guarda la respuesta de la Api en una variable.
# La API devuelve la información en formato JSON, asi que usamos el método json() para
# convertirla en un diccionario de Python y lo guardamos en response_dict.
response_dict = r.json()

# Procesa los resultados
print(response_dict.keys())

# (2) Trabajar con el directorio de respuesta.
# Con la información de la llamada a la API guardada como un diccionario, podemos trabajar
# con los datos almacenados ahí. Vamos a generar una salida que resuma la información

# Imprime el total de repositorios que nos ha devuelto el APi
print(f"Repositorios Totales: {response_dict['total_count']}")

# Explora la información sobre los repositorios.
repo_dicts = response_dict['items']
print(f"Repositorios devueltos: {len(repo_dicts)}")

# Examinamos el primer repositorio para ver si la información es correcta
# e imprimimos todas las claves del diccionario para ver que tipo de información se incluye.
# LA API de github devuelve mucha información sobre cada repositorio. Unas 78 caracteristicas.
repo_dict = repo_dicts[0]
print(f"\nLlaves: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

# Vamos a sacar las principales caracteristicas los repositorios
for repo_dict in repo_dicts:
    print('\n')
    print(f"Información principal del repositorio.".center(75,'-'))
    print(f'''Nombre: {repo_dict['name']}
Propietario: {repo_dict['owner']['login']}
Estrellas: {repo_dict['stargazers_count']}
Repositorio: {repo_dict['html_url']}
Creado: {repo_dict['created_at']}
Actualizado: {repo_dict['updated_at']}
Descripción: {repo_dict['description']}
''')

