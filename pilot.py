# Peak vs. Non Peak
# Peak = 5% on top of non-peak  
# Double Slider for Domestic and International 

import streamlit as st

#page config
st.set_page_config(
    page_title = "Infinity ∞ Club Savings Calculator",
    page_icon = "✈",
    layout="centered"
)

#display
st.title(':green[Infinity ∞ Club]')

col1,col2 = st.columns(2, gap="large")

# sliders for number of trips and trip type
with col1: 
    st.subheader('Non-Peak Period')
    num_trips_domestic_nonpeak      = st.slider("Non-Peak : Number of Domestic Trips", min_value=0, max_value=10, value=0)
    num_trips_international_nonpeak = st.slider("Non-Peak : Number of International Trips", min_value=0, max_value=10, value=0)

with col2:
    st.subheader('Peak Period')
    num_trips_domestic_peak         = st.slider("Peak : Number of Domestic Trips", min_value=0, max_value=10, value=0)
    num_trips_international_peak    = st.slider("Peak : Number of International Trips", min_value=0, max_value=10, value=0)

# checkbox for the additional baggage
st.subheader('Add-Ons')

baggage = st.checkbox("Baggage Savings (+RM20/month)")

# savings calculation function
def calculate_savings(num_trips_domestic_nonpeak,num_trips_international_nonpeak,num_trips_domestic_peak, num_trips_international_peak,baggage):

    base_savings = (num_trips_domestic_nonpeak * 377) + (num_trips_international_nonpeak *453) + ((num_trips_domestic_peak * 377)+(num_trips_domestic_peak * 0.05*1.4*377)) + ((num_trips_international_peak *453)+(num_trips_international_peak * 0.05*1.4*453)) - 1188

    if baggage:
        additional_savings = (97 * (num_trips_domestic_nonpeak+num_trips_international_nonpeak+num_trips_domestic_peak+num_trips_international_peak)) - 240
    else:
        additional_savings = 0

    total_savings = base_savings + additional_savings

    return total_savings

# Calculate savings based on user input
total_savings = calculate_savings(num_trips_domestic_nonpeak,num_trips_international_nonpeak,num_trips_domestic_peak, num_trips_international_peak,baggage)

st.divider()

col3,col4,col5 = st.columns(3, gap="large")

# Display the result
with col3:
    st.subheader('Total Estimated Savings')
with col5:
    st.header(f"RM{total_savings:.2f}","center")

st.divider()

st.caption('Savings estimates are for a return trip, based on BKIKUL(Domestic) & DMKKUL(International), as at 31st of October 2023,including an extra saving of 5% per base fare during peak period.')
st.caption('This is an estimate only and is subject to change depending on your time of travel, destination, and travel class etc.')



