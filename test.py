import streamlit as st
from mailjet_rest import Client

# Access Mailjet credentials from secrets
API_KEY = st.secrets["mailjet"]["api_key"]
API_SECRET = st.secrets["mailjet"]["api_secret"]
SENDER_EMAIL = st.secrets["mailjet"]["sender_email"]

# Initialize Mailjet client
mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

# Streamlit app layout
st.title("Mailjet Email Sender")

# Input fields
recipient = st.text_input("Recipient Email")
subject = st.text_input("Subject")
message = st.text_area("Message")

# Send email button
if st.button("Send Email"):
    if recipient and subject and message:
        data = {
            'Messages': [
                {
                    'From': {
                        'Email': SENDER_EMAIL,
                        'Name': 'Your Name'  # Optional
                    },
                    'To': [
                        {
                            'Email': recipient,
                            'Name': 'Recipient Name'  # Optional
                        }
                    ],
                    'Subject': subject,
                    'TextPart': message,
                }
            ]
        }

        # Debugging output
        st.write("Sending data:", data)

        result = mailjet.send(data=data)

        st.write("Result:", result)  # Debugging output

        if result.status_code == 200:
            st.success("Email sent successfully!")
        else:
            st.error(f"Failed to send email: {result.json()}")
    else:
        st.warning("Please fill in all fields.")

