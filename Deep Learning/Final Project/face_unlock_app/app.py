import streamlit as st
from utils import *

st.title("Face Unlock App")

option = st.sidebar.radio("Select Mode", ["Register", "Login"])

if option == "Register":
    user_name = st.text_input("Enter your name")

    if st.button("Register Face") and user_name:
        st.write("Capturing face...")
        image_path = capture_face_image("temp.jpg")
        saved_path = save_face_image(image_path, user_name)
        st.write(f"Face registered for {user_name}")
        st.image(saved_path)

elif option == "Login":
    st.write("Click to capture and verify your face.")
    
    if st.button("Login"):
        st.write("Capturing face...")
        captured_path = capture_face_image("temp_login.jpg")
        name, match = authenticate_face(captured_path)
        
        if match:
            st.write(f"Access Granted: Welcome {name}")
        else:
            st.write("Access Denied")