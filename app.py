import streamlit as st
import os
import json
import hashlib

st.title("Ransomware Detection System")
st.write("Monitor files for suspicious changes.")

folder = st.text_input("Enter test folder path")

if st.button("Scan Files"):
    if not folder or not os.path.isdir(folder):
        st.error("Please enter a valid folder path.")
    else:
        st.success("Folder found. Ready to scan.")
        st.write("Folder:", folder)
