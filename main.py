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

    if not dates and not weather:
        st.error("Please enter a valid place")

    if option == 'Temperature' and dates and weather:
        labels = {'x': 'Date', 'y': 'Temperature'}
        figure = px.line(x=dates, y=weather, labels=labels)
        st.plotly_chart(figure)

    if option == 'Sky' and dates and weather:
        image_paths = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png', 'Rain': 'images/rain.png',
                       'Snow': 'images/snow.png'}
        for d in range(0, days):
            st.image([image_paths[condition] for condition in weather[d*8:(d+1)*8]], width=85)
            st.text(f"From {dates[d*8]} to {dates[(d+1)*7]}")
