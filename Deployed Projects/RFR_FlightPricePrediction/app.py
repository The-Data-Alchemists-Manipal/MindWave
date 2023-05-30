import numpy as np
import pandas as pd
import pickle
import streamlit as st
from datetime import datetime, timedelta
import base64

model = pickle.load(open('./model/flight_prediction.pkl', 'rb'))

def flight_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    
    rounded_value = round(prediction[0], 2)
    return rounded_value

def main():

    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1614851099511-773084f6911d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    with st.container():
        st.markdown(
            """
            <h1 style='text-align: center;'>Flight Price Prediction</h1>
            """,
            unsafe_allow_html=True
        )
        
        # Source
        sources = ['Chennai', 'Delhi', 'Kolkata', 'Mumbai']

        selected_source = st.selectbox('Select Source', sources)
        source_mapping = {source: 1 if source == selected_source else 0 for source in sources}
        Source = list(source_mapping.values())

        # Destination
        destinations = ['Cochin', 'Delhi', 'Hyderabad', 'Kolkata']

        selected_destination = st.selectbox('Select Destination', destinations)
        destination_mapping = {destination: 1 if destination == selected_destination else 0 for destination in destinations}
        Destination = list(destination_mapping.values())

        # Time
        dep_date = st.date_input("Departure Date", value=datetime.now().date())
        dep_time = st.time_input("Departure Time", value=datetime.now().time())
        arrival_date = st.date_input("Arrival Date", value=datetime.now().date())
        arrival_time = st.time_input("Arrival Time", value=datetime.now().time())

        Journey_Day = dep_date.day
        Journey_Month = dep_date.month
        Departure_Hour = dep_time.hour
        Departure_Min = dep_time.minute
        Arrival_Hour = arrival_time.hour
        Arrival_Min = arrival_time.minute

        Departure_Datetime = datetime.combine(dep_date, dep_time)
        Arrival_Datetime = datetime.combine(arrival_date, arrival_time)
        duration = Arrival_Datetime - Departure_Datetime

        Duration_Hours = duration.days * 24 + duration.seconds // 3600
        Duration_Minutes = (duration.seconds % 3600) // 60

        # Stops
        Total_Stops = st.number_input("Number of Stops", min_value=0, step=1, value=0)

        # Airline
        airlines = ['Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business', 'Multiple carriers',
                'Multiple carriers Premium economy', 'SpiceJet', 'Trujet', 'Vistara', 'Vistara Premium economy']

        selected_airline = st.selectbox('Select Airline', airlines)
        airline_mapping = {airline: 1 if airline == selected_airline else 0 for airline in airlines}
        Airlines = list(airline_mapping.values())


        journey_input = [Total_Stops, Journey_Day, Journey_Month, Departure_Hour, Departure_Min,
                        Arrival_Hour, Arrival_Min, Duration_Hours, Duration_Minutes]
        airline_input = Airlines
        source_input = Source
        destination_input = Destination

        Input = journey_input + airline_input + source_input + destination_input

        price_prediction = ''

        if st.button('Predict Price'):
            price_prediction = flight_prediction(Input)
            st.markdown(
                """
                <h3 style='text-align: center;'>You will have to pay approximately Rs. {}</h3>
                """.format(price_prediction),
                unsafe_allow_html=True
            )


if __name__ == '__main__':
    main()