import streamlit as st
import streamlit.components.v1 as components
import os

# Set page configuration
st.set_page_config(page_title="AR Wallpaper Viewer", layout="wide")
st.title("📱 Marshal AR Wallpaper Experience")

st.markdown("""
Select a wallpaper and click **View in Your Room** to preview it on your wall in real time using Augmented Reality.
""")

# Read the HTML file
html_file = os.path.join(os.getcwd(), "webar.html")
if os.path.exists(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    components.html(html, height=700)
else:
    st.error("⚠️ webar.html not found.")