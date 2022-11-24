import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
##### ajouter des caractéristiques de style pour la police de la side bar
font_sidebar_style="""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Roboto:wght@100&display=swap');
    
    html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
    
    </style> 

"""
st.markdown(font_sidebar_style,unsafe_allow_html=True)
######
###### titre de la page

st.title("Cars features")
st.image("https://img.freepik.com/vecteurs-premium/types-voitures-conception-transport-fond-blanc-illustration_384401-12.jpg")

######
###### side bar
with st.sidebar :
    st.markdown('Some useful definitions :')

    with st.expander("mpg"):
        col1,col2=st.columns([2,1]) #on a 2 colonnes, entre crochet on indique le 'poids' de la première colonne puis le poids de la deuxième
        with col1 :
            st.write("""
                MPG means miles per gallon, which is essentially how much fuel you burn in comparison to the distance you cover.
                Finding a good MPG depends on the car's brand and model, as well as whether it's new or used. 
                There are other variables to consider too, including vehicle size, engine, and driving conditions.
            """)
        with col2:
            st.image("https://www.stocksignes.fr/4568-7090-thickbox/parking-.jpg",use_column_width="always")


    with st.expander("cubic inch"):
        col1,col2=st.columns(2)
        with col1 :
            st.write("""
                The cubic inch is a unit of measurement for volume in the Imperial units and United States systems.
                It is the volume of a cube with each of its three dimensions (length, width, and depth) being one inch long.
                The cubic inch of a motor, in most cases, is a reference to the size of the motor.
            """)
        with col2:
            st.image("https://us.123rf.com/450wm/ahasoft2000/ahasoft20001703/ahasoft2000170302699/74170959-ic%C3%B4ne-de-vecteur-de-cube-symbole-noir-plat-le-pictogramme-est-isol%C3%A9-sur-un-fond-blanc-con%C3%A7u-pour-les.jpg")       
            
    with st.expander("hp"):
        col1,col2=st.columns(2)
        with col1 :
            st.write("""
                Horsepower refers to the power an engine produces.
                It's calculated through the power needed to move 550 pounds one foot in one second or by the power needs to move 33,000 pounds one foot in one minute.
            """)
        with col2:
            st.image("https://i.pinimg.com/564x/98/55/17/985517418b46749180709b0a85fd5bbe.jpg")       
                
    with st.expander("time to 60"):
        col1,col2=st.columns(2)
        with col1 :
            st.write("""
                The time it takes a vehicle to accelerate from 0 to 60 miles per hour (0 to 97 km/h or 0 to 27 m/s), often said as just "zero to sixty", is a commonly used performance measure for automotive acceleration in the United States and the United Kingdom.
            """)
        with col2:
            st.image("https://png.pngtree.com/png-vector/20190307/ourlarge/pngtree-speed-meter-for-automobile-car-or-byke-png-image_781921.jpg")       
######
            
######     
        
        
        
link="https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

df_cars=pd.read_csv(link)
###

st.subheader("1 - Graph avec sélection des continent dans un radiobox.")
st.markdown("sélection multiple impossible")


#### création des boutons de sélection des différents continents
continent_liste=np.append(df_cars['continent'].unique(),'All') #df_cars['continent'].unique() est un numpy array, donc pour lui ajouter une valeur il faut utiliser la syntaxe np.append(array_de_base,valeur_à_ajouter)

continent=st.radio(
    "select a continent",
    continent_liste,
    key=1
)
######
###### indiquer le graph a afficher en fonction du bouton selectionné
st.write(f"Consommation en mpg en fonction du poids de la voiture pour le continent : {continent}")
if continent!='All':
    df_chart1=df_cars[df_cars['continent']==continent]
    #plt.figure(figsize=(8,8))
    chart_1=sns.scatterplot(data=df_chart1,x='weightlbs',y='mpg',hue='continent')
    #plt.title('consommation en mpg en fonction du poids de la voiture')
    st.pyplot(chart_1.figure)
else:
    chart_1=sns.scatterplot(data=df_cars,x='weightlbs',y='mpg',hue='continent')
    st.pyplot(chart_1.figure)

    
st.text("Conclusion : plus les voitures sont lourdes, plus moins on fait de miles par")

######

st.subheader('2 - Avec un graph plotly.express où on peut selectionner directement les continents sans manip supplémentaire')

chart_2= px.scatter(df_cars,x='hp',y='cubicinches',color='continent',title='cubicinches vs horse power ')
st.plotly_chart(chart_2)

st.text("""En Europe et au Japon, les voitures on des cubicinches et des puissances en chevaux équivalentes.
En revanche, aux Etats Unis, les voitures ont pluôt de grosses cubicinches""")
######

###### avec une liste déroulante
st.subheader("3 - avec une liste déroulante")
option_continent = st.selectbox(
    'select a continent',
    continent_liste)

st.write(option_continent)
if option_continent!='All':
    fig=plt.figure(figsize=(10,5))
    sns.regplot(x='time-to-60',y='hp',data=df_cars[df_cars['continent'].str.contains(option_continent)])
    st.pyplot(fig)
else:
    fig=plt.figure(figsize=(10,5))
    sns.regplot(data=df_cars,x='time-to-60',y='hp')
    st.pyplot(fig)

st.text("Conclusion : plus on a de chevaux, plus on atteint le 60miles/h en peu de temps")


#####coté plotly.express mettre un animation_frame
st.subheader("4 - Histogramme animé dans le temps")

#continent_liste=np.append(df_cars['continent'].unique(),'All')

continent_animation=st.radio(
    "select a continent",
    continent_liste,
    key=2)

if continent_animation!='All':
    animated_histogram=px.histogram(df_cars[df_cars['continent'].str.contains(continent_animation)],x='mpg',title='distribution du time-to-60',range_y=[0,35],animation_frame='year')
    st.plotly_chart(animated_histogram)
else:
    animated_histogram=px.histogram(df_cars,x='mpg',title='distribution du time-to-60',range_y=[0,35],animation_frame='year')
    st.plotly_chart(animated_histogram)  



#####mettre un slider sur les years