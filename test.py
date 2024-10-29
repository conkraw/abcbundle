import streamlit as st
from mailjet_rest import Client

# Access Mailjet credentials from secrets
API_KEY = st.secrets["mailjet"]["api_key"]
API_SECRET = st.secrets["mailjet"]["api_secret"]
SENDER_EMAIL = st.secrets["mailjet"]["sender_email"]

from mailjet_rest import Client

recipient = "ckrawiec@pennstatehealth.psu.edu"
subject = "Test Subject"
message = "Test Message"

# Initialize Mailjet client
mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

data = {
    'Messages': [
        {
            'From': {
                'Email': SENDER_EMAIL,
                'Name': 'Your Name'
            },
            'To': [
                {
                    'Email': recipient,
                    'Name': 'Recipient Name'
                }
            ],
            'Subject': subject,
            'TextPart': message,
        }
    ]
}

result = mailjet.send(data=data)

print(f"Status Code: {result.status_code}")
print("Response:", result.json())

