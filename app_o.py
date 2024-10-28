import streamlit as st

# Function to create a boxed section
def box_section(title):
    return f"""
    <div style="border: 1px solid #0072B8; border-radius: 5px; padding: 10px; margin-bottom: 20px;">
        <h4 style="margin: 0; color: #0072B8;">{title}</h4>
    </div>
    """

st.title("Airway Bundle Checklist")

# Timing of Intubation Section
st.markdown(box_section("Timing of Intubation"), unsafe_allow_html=True)

# Multi-select for timing of intubation
when_intubate = st.multiselect(
    "When will we intubate? (Describe timing of airway management):",
    ['Prior to procedure', 'Mental Status Changes', 
     'Hypoxemia Refractory to CPAP', 'Ventilation failure refractory to NIV', 
     'Loss of Airway Protection', 'Other'],
    key="when_intubate"
)

# Check if "Hypoxemia Refractory to CPAP" is selected
if "Hypoxemia Refractory to CPAP" in when_intubate:
    spo2_input = st.text_input("SPO2 Less Than?:", key="spo2_input")

# Submit button
submit = st.button("Submit")

# Process submission
if submit:
    st.success("Form submitted successfully!")
    # Here, you would handle the form data as needed

# To run this app, use the command:
# streamlit run app.py
