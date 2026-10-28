import streamlit as st
import os
import hashlib

st.title("Ransomware Detection System")
st.write("Upload test files to check for suspicious changes.")

uploaded_files = st.file_uploader(
    "Choose test files",
    accept_multiple_files=True
)

if st.button("Scan Files"):
    if not uploaded_files:
        st.warning("Please upload at least one test file.")
    else:
        for file in uploaded_files:
            data = file.getvalue()
            file_hash = hashlib.sha256(data).hexdigest()
            st.write(f"File: {file.name}")
            st.write(f"SHA-256: {file_hash}")

        st.success("Scan completed.")
