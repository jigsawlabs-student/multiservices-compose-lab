import streamlit as st
import requests 

response = requests.get('api/locations')
response.json()

st.write("""
# My first app
Hello *world!*
""")
