import firebase_admin
from firebase_admin import credentials, firestore

firebase_creds = {
    "project_id": st.secrets["firebase"]["api_key"],
    "private_key_id": st.secrets["firebase"]["api_secret"],
}

# Initialize Firebase Admin
cred = credentials.Certificate(firebase_creds)
firebase_admin.initialize_app(cred)
db = firestore.client()

st.title("Email Trigger")

to_email = st.text_input("conkraw@gmail.com")
subject = st.text_input("Email Subject")
message = st.text_area("Email Message")

if st.button("Send Email"):
    # Create the email document in Firestore
    email_data = {
        "to": to_email,
        "message": {
            "subject": subject,
            "html": message,
        }
    }
    db.collection('mail').add(email_data)
    st.success("Email trigger sent!")
