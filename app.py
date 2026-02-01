import streamlit as st
import joblib
import pandas as pd
import numpy as np

# 1. Load the trained model
# Ensure 'fault_detector_model.pkl' is in the same folder
try:
    model = joblib.load('fault_detector_model.pkl')
except FileNotFoundError:
    st.error("Error: 'fault_detector_model.pkl' not found. Please make sure you saved the model in the same folder.")
    st.stop()

# 2. App Title and Description
st.title("🏭 IoT Sensor Fault Detection")
st.write("Enter sensor readings below to check for equipment faults.")

# 3. Sidebar for User Inputs
st.sidebar.header("Input Sensor Data")

def user_input_features():
    # We need inputs for all 6 features used in training
    vibration = st.sidebar.slider('Vibration (Raw)', 0.0, 100.0, 50.0)
    temperature = st.sidebar.slider('Temperature (Raw)', 100.0, 300.0, 200.0)
    
    # In a real system, these are calculated automatically. 
    # For this demo, we let the user estimate them.
    vib_roll_mean = st.sidebar.slider('Vibration (Rolling Mean)', 0.0, 100.0, 50.0)
    temp_roll_mean = st.sidebar.slider('Temperature (Rolling Mean)', 100.0, 300.0, 200.0)
    
    vib_roll_std = st.sidebar.slider('Vibration (Std Dev)', 0.0, 50.0, 5.0)
    temp_roll_std = st.sidebar.slider('Temperature (Std Dev)', 0.0, 50.0, 10.0)

    data = {
        'vibration': vibration,
        'temperature': temperature,
        'vibration_roll_mean': vib_roll_mean,
        'temp_roll_mean': temp_roll_mean,
        'vibration_roll_std': vib_roll_std,
        'temp_roll_std': temp_roll_std
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# 4. Display User Input
st.subheader("Current Sensor Readings")
st.write(input_df)

# 5. Make Prediction
if st.button("Analyze Status"):
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)

    st.subheader("Diagnosis:")
    
    if prediction[0] == 1:
        st.error(f"⚠️ FAULT DETECTED! (Confidence: {probability[0][1]*100:.2f}%)")
        st.write("The equipment is showing abnormal behavior. Check for Overheating or High Vibration.")
    else:
        st.success(f"✅ Normal Operation (Confidence: {probability[0][0]*100:.2f}%)")
        st.write("System is running within safe parameters.")
