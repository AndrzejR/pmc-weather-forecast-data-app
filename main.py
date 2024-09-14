import streamlit as st
import plotly.express as px
import backend

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        dates, weather = backend.get_weather_data(place, days, option)

        if option == 'Temperature':
            labels = {'x': 'Date', 'y': 'Temperature'}
            figure = px.line(x=dates, y=weather, labels=labels)
            st.plotly_chart(figure)

        if option == 'Sky':
            image_paths = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png', 'Rain': 'images/rain.png',
                           'Snow': 'images/snow.png'}
            for d in range(0, days):
                st.image([image_paths[condition] for condition in weather[d*8:(d+1)*8]], width=85)
                st.text(f"From {dates[d*8]} to {dates[(d+1)*7]}")

    except ValueError:
        pass
