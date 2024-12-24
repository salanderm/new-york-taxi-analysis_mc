import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


# Borough and location handling
st.header("Select Location")
borough = st.selectbox("Select a Borough", ["Bronx", "Manhattan", "Brooklyn", "Queens", "Staten Island","Unknown"])
transaction_month= st.selectbox("Enter the month", [1,2,3,4,5,6,7,9,10,11,12])
transaction_day = st.selectbox("Enter the day", [1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])
transaction_hour = st.selectbox("Enter the hour", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
transaction_week_day = st.selectbox("Enter the weekday", [0,1,2,3,4,5,6])
weekend = st.selectbox("Is it weekend?", [0,1])
is_holiday = st.selectbox("Is it holiday?", [0,1])
temp = st.number_input("Enter the temperature")
humidity = st.number_input("Enter the humidity")
windspeed = st.number_input("Enter the windspeed")
cloudcover = st.number_input("Enter the amount of cloudcover")
precip = st.number_input("Enter the precipitation amount")
"""
'transaction_month', 'transaction_day',
       'transaction_hour', 'transaction_week_day', 'weekend', 'is_holiday', 'Borough']
input_features = categorical_features + ['temp', 'humidity', 'windspeed', 'cloudcover',
       'precip']
"""