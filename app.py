import streamlit as st
import hashlib
import json

st.title("Ransomware Detection System")
st.write("Safely detect new or modified files by comparing hashes.")

baseline_file = st.file_uploader(
    "Upload baseline.json",
    type=["json"],
    key="baseline"
)

test_files = st.file_uploader(
    "Upload files to scan",
    accept_multiple_files=True,
    key="tests"
)

if st.button("Scan Files"):
    if baseline_file is None:
        st.error("Please upload baseline.json first.")
    elif not test_files:
        st.warning("Please upload at least one test file.")
    else:
        try:
            baseline = json.load(baseline_file)
            if not isinstance(baseline, dict):
                raise ValueError("Baseline must be a JSON object.")

            for file in test_files:
                digest = hashlib.sha256(file.getvalue()).hexdigest()
                old_digest = baseline.get(file.name)

                if old_digest is None:
                    st.warning(f"New file: {file.name}")
                elif old_digest != digest:
                    st.error(f"Modified file: {file.name}")
                else:
                    st.success(f"No change: {file.name}")

            st.info("Scan completed.")
        except (json.JSONDecodeError, ValueError) as error:
            st.error(f"Could not read baseline.json: {error}")
