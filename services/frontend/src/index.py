import streamlit as st
import requests
url = 'http://api:5000/locations'
response = requests.get(url)
locations = response.json()

st.write("""
# My first app
Hello *world!*
""")

for location in locations['locations']:
    st.write(location[1])
