# El Requests permite a un programa de Python solicitar información a un sitio web y
# examinar la respuesta.
import requests

# Hace una llamada al Api de GitHub y guarda la respuesta.
# Github va por la tercera versión del api asi que usamos esa.
url = 'https://api.github.com/search/repositories?q=langage:python&sort=starts'
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
response_dic = r.json()

# Procesa los resultados
print(response_dic.keys())
