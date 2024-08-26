import streamlit as st
import datetime
import requests
import geocoder


url = st.secrets['url']
# url = 'https://taxifare.lewagon.ai/predict'

st.title('NY Fare Prediction')

with st.form('predict'):
    d = st.date_input("Date of ride", datetime.date(2020, 7, 6))
    t = st.time_input("Time of ride", datetime.time(19,30))
    pickup_location=st.text_input("Pickup location", value=('Central Park'))
    dropoff_location=st.text_input("Dropoff location", value=('Chinatown'))
    # pickup_longitude = st.number_input("Pickup longitude", value=(-73.950655))
    # pickup_latitude = st.number_input("Pickup latitude", value=(40.783282))
    # dropoff_longitude = st.number_input("Dropoff longitude", value=(-73.984365))
    # dropoff_latitude = st.number_input("Dropoff latitude", value=(40.769802))
    passenger_count = st.number_input("Number of passengers", value=(2))
    pickup_datetime = f"{d} {t}"

    submit = st.form_submit_button('predict fare')


if submit:
    with st.spinner('Computing fare...'):
        pickup = geocoder.mapbox(f"{pickup_location},NY", key=st.secrets['mapbox'])
        dropoff = geocoder.mapbox(f"{dropoff_location},NY", key=st.secrets['mapbox'])

        params = {
            "pickup_datetime": pickup_datetime,
            "pickup_longitude": pickup.json['lng'],
            "pickup_latitude": pickup.json['lat'],
            "dropoff_longitude": dropoff.json['lng'],
            "dropoff_latitude": dropoff.json['lat'],
            "passenger_count": passenger_count
        }

        response = requests.get(url, params=params)
        fare = response.json()
        st.info(f"Predicted Fare is: {fare['fare']}", icon="🚕")


'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
    # st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...(https://taxifare.lewagon.ai/predict)')

'''

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
