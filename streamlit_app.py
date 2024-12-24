import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


# Borough and location handling
st.header("Select Location")
borough = st.selectbox("Select a Borough", ["Bronx", "Manhattan", "Brooklyn", "Queens", "Staten Island","Unknown"])
transaction_month= st.text_input("Enter the month as int")

"""
'transaction_month', 'transaction_day',
       'transaction_hour', 'transaction_week_day', 'weekend', 'is_holiday', 'Borough']
input_features = categorical_features + ['temp', 'humidity', 'windspeed', 'cloudcover',
       'precip']
"""