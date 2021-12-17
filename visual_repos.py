'''Visualiza los repositorios que tienen más estrellas y poder hacer un gráfico interactivo
en el que pulsando en la barra se pueda ir a la web del proyecto.'''

import requests

# Importamos la clase Bar y el módulo offline. No se importa la clase Layout porque vamos a usar
# la estrategia del diccionario para definir la disposición.
# from plotly.graph_objs import Bar
from plotly import offline

# Hace una llamada al Api de Github y guarda la respuesta para ver que funciona correctamente.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Procesa los resultados basándose en los repositorios y a las estrellas.
response_dict = r.json()
repo_dicts = response_dict['items']
nombre_repositorios, estrellas = [], []
for repo_dict in repo_dicts:
    nombre_repositorios.append(repo_dict['name'])
    estrellas.append(repo_dict['stargazers_count'])

# Hace la visualización
datos = [{
    'type': 'bar',
    'x': nombre_repositorios,
    'y': estrellas,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
}]

# 'marker' es opcional, pero personaliza el color de las barras del gráfico.
# Le ponemos un color azul personalizado y un contorno gris oscuro con una anchura de línea
# de 1,5 pixeles. También ponemos la opacidad de las barras en 0,6 para suavizar un poco
# la apariencia del gráfico.

mi_grafico = {
    'title': 'Los proyectos con más estrellas en Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repositorios',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Estrellas',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
},
}

fig = {'data': datos, 'layout': mi_grafico}
offline.plot(fig, filename='python_repositorios.html')
