import streamlit as st

# Age to ETT size mapping
age_to_ett_mapping = {
    "": "",
    "Premature": "3.0",
    "Newborn": "3.5",
    "1 month old": "3.5",
    "2 month old": "3.5",
    "3 month old": "4.0",
    "4 month old": "4.0",
    "5 month old": "4.0",
    "6 month old": "4.0",
    "1 year old": "4.5",
    "2 year old": "4.5",
    "3 year old": "4.5",
    "4 year old": "5.0",
    "5 year old": "5.0",
    "6 year old": "5.0",
    "7 year old": "6.0",
    "8 year old": "6.0",
    "9 year old": "6.0",
    "10 year old": "6.0",
    "11 year old": "6.5",
    "12 year old": "6.5",
    "13 year old": "6.5",
    "14 year old": "6.5",
    "15 year old": "6.5",
    "16 year old": "7.0",
    "17 year old": "7.0",
    "18 year old": "7.0"
}

# Function to update ETT size based on selected age
def update_ett_size_based_on_age():
    selected_age = st.session_state.get("age_select")
    if selected_age:
        # Set ETT size based on age
        st.session_state['ett_size'] = age_to_ett_mapping.get(selected_age, '')

# Create a Streamlit app to demonstrate
st.title("Dynamic ETT Size Based on Age")

# Select patient's age
age_select = st.selectbox("Select Patient Age", list(age_to_ett_mapping.keys()), key="age_select")

# Dynamically update ETT size when age is selected
update_ett_size_based_on_age()

# Show the dynamic ETT size
ett_size = st.selectbox("ETT Size Based on Age", options=['', '3.0', '3.5', '4.0', '4.5', '5.0', '6.0', '6.5', '7.0'], key="ett_size", index=['', '3.0', '3.5', '4.0', '4.5', '5.0', '6.0', '6.5', '7.0'].index(st.session_state['ett_size']) if st.session_state['ett_size'] else 0)

# Display the result
st.write(f"Selected Age: {age_select}")
st.write(f"Suggested ETT Size: {st.session_state['ett_size']}")

