import streamlit as st
import plotly.express as px
import backend

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    dates, weather = backend.get_weather_data(place, days, option)
    if option == 'Temperature':
        labels = {'x': 'Date', 'y': 'Temperature'}
        figure = px.line(x=dates, y=weather, labels=labels)
        st.plotly_chart(figure)

    if option == 'Sky':
        st.image(['images/clear.png', 'images/cloud.png', 'images/rain.png', 'images/snow.png'], width=100)
        # for w in weather:
        #     match w:
        #         case 'Clear':
        #             st.image('.\images\clear.png')
        #         case 'Clouds':
        #             st.image('.\images\cloud.png')
        #         case 'Rain':
        #             st.image('.\images\\rain.png')
        #         case 'Snow':
        #             st.image('.\images\snow.png')
