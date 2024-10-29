import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

# Initialize Firebase if not already done
if 'firebase_initialized' not in st.session_state:
    firebase_key = st.secrets["FIREBASE_KEY"]
    cred = credentials.Certificate(json.loads(firebase_key))
    
    try:
        firebase_admin.initialize_app(cred)
        st.session_state.firebase_initialized = True
    except ValueError as e:
        if "already exists" in str(e):
            pass  # App is already initialized
        else:
            st.error(f"Failed to initialize Firebase: {str(e)}")

# Access Firestore
if 'db' not in st.session_state:
    try:
        st.session_state.db = firestore.client()
    except Exception as e:
        st.error(f"Failed to connect to Firestore: {str(e)}")

# Set the current section for your app (replace with your actual logic)
st.session_state.section = 6  # For testing, set the section to 6

if st.session_state.section == 6:
    st.title("Download ABC Form")
    
    # Input fields for email data
    to_email = st.text_input("Email")
    subject = st.text_input("Email Subject")
    message = st.text_area("Email Message")
    
    col1, col2, col3 = st.columns(3)

    # Initialize session state variables for form submission
    if 'doc_file' not in st.session_state:
        st.session_state.doc_file = None

    with col3: 
        if st.button("Submit"):
            # Upload data to Firebase
            db = st.session_state.db  # Access the Firestore client from session state
            
            # Prepare email data to upload
            email_data = {
                "to": to_email,
                "message": {
                    "subject": subject,
                    "html": message,
                }
            }

            try:
                db.collection("N4KFORMP").add(email_data)  # Add email data to the Firestore collection
                st.success("Form submitted successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.exception(e)  # Print the stack trace for debugging

