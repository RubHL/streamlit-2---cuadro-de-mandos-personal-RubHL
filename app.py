import streamlit as st
import pandas as pd
import altair as alt

# URL con la lista de pasajeros del Titanic
# https://github.com/KeithGalli/pandas/blob/master/pokemon_data.csv
URL = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"
datos = pd.read_csv(URL)

st.title('Datos sobre Pokémons')

# Define el tipo de gráfico a mostrar en el cuadro de mandos
tipo_grafico = st.sidebar.selectbox('Seleccione el tipo de gráfico',
                                    ('Gráfico de barras', 'Gráfico de dispersión', 'Gráfico de líneas'))

# Gráfico de barras que muestra la cantidad de Pokemon por tipo
if tipo_grafico == 'Gráfico de barras':
    st.write('#### Cantidad de Pokemon por tipo')
    tipo_count = datos['Type 1'].value_counts()
    chart = alt.Chart(tipo_count.reset_index()).mark_bar().encode(
        x='Type 1',
        y='index'
    )
    st.altair_chart(chart, use_container_width=True)

# Gráfico de dispersión de puntos para visualizar la relación entre los puntos de ataque y los puntos de defensa de los Pokemon
elif tipo_grafico == 'Gráfico de dispersión':
    st.write('#### Gráfico de dispersión de puntos para visualizar la relación entre los puntos de ataque y los puntos de defensa de los Pokemon.')
    scatter_chart = alt.Chart(datos).mark_point().encode(
        x='Attack:Q',
        y='Defense:Q',
        color='Type 1:N',
        tooltip=['Name']
    ).interactive()
    st.altair_chart(scatter_chart, use_container_width=True)


# Cantidad de Pokemon introducidos en cada generación
else:
    st.write('#### Cantidad de Pokemon introducidos en cada generación')
    gen_count = datos['Generation'].value_counts().sort_index().reset_index()
    gen_count.columns = ['Generation', 'Count']

    bar_chart = alt.Chart(gen_count).mark_bar().encode(
        x='Generation:N',
        y='Count:Q'
    ).properties(
        width=600,
        height=400
    ).interactive()

    st.altair_chart(bar_chart, use_container_width=True)