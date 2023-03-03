# 📈 Cuadro de mandos personal 📊
 
> Usa este repositorio para crear un cuadro de mandos personal con Streamlit. Documenta los siguientes apartados del README.
> Incluye en tu README la url de donde has publicado tu aplicación. Pon la `url` también en el `About` de tu repositorio.

## Objetivo
Diseño de un cuadro de mandos personal para visualización e interacción con un conjunto de datos.

## Los datos
Elige un conjunto de datos que te interese: educación, deportes, trabajo, música, econocomía, etc. 
__
El conjunto de datos seleccionado contiene información de Pokémons de distintas generaciones.

## Búsqueda de los datos
Busca una fuente para tus datos. Puedes usar una API de un portal de datos abiertos, un conjunto ya publicado, recopilar personalmente datos por scraping, etc.
___

A través del sitio web Kaggle, he buscado diversos datasets.


## Documentación de los datos
Documenta los datos que vas a usar y su origen. De dónde los has sacado, fuentes, etc. Describe los campos, los valores, las unidades, etc.
___
Los datos utilizados en este proyecto provienen del conjunto de datos "Pokemon with stats" de Kaggle. El conjunto de datos contiene información sobre 800 Pokémon diferentes, incluyendo su tipo, puntos de ataque, puntos de defensa, puntos de velocidad y más. El archivo original se puede encontrar en: https://www.kaggle.com/abcsds/pokemon

El archivo utilizado en este proyecto es una versión limpiada del conjunto de datos original, que se encuentra en: https://github.com/KeithGalli/pandas/blob/master/pokemon_data.csv

El conjunto de datos contiene los siguientes campos:

| Columna      | Descripción                                           |
|--------------|-------------------------------------------------------|
| Name         | Nombre del Pokemon                                    |
| Type 1       | Tipo primario del Pokemon                             |
| Type 2       | Tipo secundario del Pokemon (opcional)                 |
| Total        | Puntos totales de los atributos del Pokemon            |
| HP           | Puntos de salud del Pokemon                            |
| Attack       | Puntos de ataque del Pokemon                           |
| Defense      | Puntos de defensa del Pokemon                          |
| Sp. Atk      | Puntos de ataque especial del Pokemon                  |
| Sp. Def      | Puntos de defensa especial del Pokemon                 |
| Speed        | Puntos de velocidad del Pokemon                        |
| Generation   | Generación a la que pertenece el Pokemon               |
| Legendary    | Indica si el Pokemon es legendario o no                |

## Prepara tu aplicación.
La aplicación se llamará `app.py`. Añade un `requirements.txt` con las dependencias de tu aplicación. Ve actualizándolo a medida que vayas añadiendo librerías.
___
Lista de dependencias:
````
pandas
streamlit
altair==4.2.2
attrs==22.2.0
blinker==1.5
cachetools==5.3.0
certifi==2022.12.7
charset-normalizer==3.0.1
click==8.1.3
decorator==5.1.1
entrypoints==0.4
gitdb==4.0.10
GitPython==3.1.31
idna==3.4
importlib-metadata==6.0.0
importlib-resources==5.12.0
Jinja2==3.1.2
jsonschema==4.17.3
markdown-it-py==2.2.0
MarkupSafe==2.1.2
mdurl==0.1.2
numpy==1.24.2
packaging==23.0
pandas==1.5.3
Pillow==9.4.0
pkgutil_resolve_name==1.3.10
protobuf==3.20.3
pyarrow==11.0.0
pydeck==0.8.0
Pygments==2.14.0
Pympler==1.0.1
pyrsistent==0.19.3
python-dateutil==2.8.2
pytz==2022.7.1
pytz-deprecation-shim==0.1.0.post0
requests==2.28.2
rich==13.3.1
semver==2.13.0
six==1.16.0
smmap==5.0.0
streamlit==1.18.1
toml==0.10.2
toolz==0.12.0
tornado==6.2
typing_extensions==4.5.0
tzdata==2022.7
tzlocal==4.2
urllib3==1.26.14
validators==0.20.0
watchdog==2.2.1
zipp==3.14.0
````


## Carga y análisis de conjunto de dato con pandas
Carga el conjunto de datos en un dataframe de pandas y realiza un análisis exploratorio de los datos.
___
Para cargar el conjunto de datos en un dataframe de pandas usamos la función read_csv() de pandas.


## Visualización de los datos
Prepara visualizaciones diferentes del dataframe en texto (tablas) o gráficas (histogramas, barras, etc.). Puedes usar matplotlib, seaborn, plotly, etc.
___
1. Gráfico de barras: Se utiliza para mostrar la cantidad de Pokemon por tipo. Este gráfico se genera utilizando la biblioteca Altair.

2. Gráfico de dispersión: Se utiliza para visualizar la relación entre los puntos de ataque y los puntos de defensa de los Pokemon. El gráfico también utiliza diferentes colores para indicar el tipo de Pokemon y un tooltip para mostrar el nombre del Pokemon. Este gráfico también se genera utilizando la biblioteca Altair.

3. Gráfico de barras: Se utiliza para mostrar la cantidad de Pokemon introducidos en cada generación. Este gráfico también se genera utilizando la biblioteca Altair.

## Diseña la interacción que van a tener tus datos
Qué inputs y outputs tendrán tus datos. 
___

Inputs:

* Tipo de gráfico seleccionado a través del cuadro de selección en la barra lateral.

Outputs:

* Gráfico de barras que muestra la cantidad de Pokemon por tipo.
* Gráfico de dispersión de puntos que muestra la relación entre los puntos de ataque y defensa de los Pokemon, con el color del punto indicando el tipo de Pokemon y un tooltip que muestra el nombre del Pokemon.
* Gráfico de barras que muestra la cantidad de Pokemon introducidos en cada generación.

## Prepara la aplicación (cuadro de mandos) con Streamlit
Prepara y prueba la aplicación.
___
Ejecutamos:
````
 streamlit run app.py 
````

## Publica la aplicación.
Publica la aplicación en Streamlit Cloud, en Heroku o en el servicio que prefieras https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app
