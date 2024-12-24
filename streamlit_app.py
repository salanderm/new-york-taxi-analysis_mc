import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Session state initialization
if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False
if "predicted_amt" not in st.session_state:
    st.session_state.predicted_amt = None

def reset_app():
    st.session_state.prediction_done = False
    st.session_state.predicted_amt = None

# Main app
if not st.session_state.prediction_done:
    st.title("NYC Taxi Analysis App🚖")

    st.header("Please enter the inputs below")
    # Borough and location handling
    borough = st.selectbox("Select a Borough", ["Bronx", "Manhattan", "Brooklyn", "Queens", "Staten Island", "Unknown"])
    transaction_month = st.selectbox("Enter the month", list(range(1, 13)))
    transaction_day = st.selectbox("Enter the day", list(range(1, 32)))
    transaction_hour = st.selectbox("Enter the hour", list(range(24)))
    transaction_week_day = st.selectbox("Enter the weekday", list(range(7)))
    weekend = st.selectbox("Is it weekend?", [0, 1])
    is_holiday = st.selectbox("Is it holiday?", [0, 1])
    temp = st.number_input("Enter the temperature")
    humidity = st.number_input("Enter the humidity")
    windspeed = st.number_input("Enter the windspeed")
    cloudcover = st.number_input("Enter the amount of cloudcover")
    precip = st.number_input("Enter the precipitation amount")

    # Load column holders and model
    X_test = pd.read_csv("dummy_column_holder.csv")
    nyc_class = pd.read_csv("nyc_class.csv")

    pre_input_array = [transaction_month, transaction_day, transaction_hour, transaction_week_day, weekend, is_holiday, temp, humidity, windspeed, cloudcover, precip]

    def get_location(loc):
        int_csv = pd.read_csv("data/taxi_zone_lookup.csv")[['LocationID', 'Borough']]
        return int_csv[int_csv["Borough"] == loc].values[0][0]

    def get_location_array(loc_id, column_names):
        new_list = list(np.zeros(len(column_names)))
        loc_index = column_names.index(f'PULocationID_{loc_id}')
        new_list[loc_index] = 1.0
        return list(map(float, new_list))

    def get_borough_array(borough):
        borough_lookup = list(nyc_class["Borough"].value_counts().keys())
        b_count = len(borough_lookup)
        b_count_list = list(map(float, list(np.zeros(b_count))))
        b_count_list[borough_lookup.index(borough)] = 1.0
        return b_count_list

    column_names = [x for x in X_test.columns if x.startswith('PULocationID')]
    loc_id = get_location(borough)
    loc_array = get_location_array(loc_id, column_names)
    borough_array = get_borough_array(borough)

    # Load the model
    with open("model_at_hand.pkl", "rb") as f:
        model_at_hand = pickle.load(f)

    input_array = pre_input_array + loc_array + borough_array
    input_array = np.array(input_array).reshape(1, -1)

    if st.button("Predict"):
        predicted_amt = model_at_hand.predict(input_array)[0]
        st.session_state.prediction_done = True
        st.session_state.predicted_amt = predicted_amt

else:
    st.header(f"💵 PREDICTED AMOUNT: ${st.session_state.predicted_amt:.2f}")
    if st.button("🔙 Back"):
        reset_app()
