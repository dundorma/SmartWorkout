import streamlit as st
from PIL import Image
from camera_input_live import camera_input_live


# Set up the Streamlit app layout
st.title("Camera Preview with Text Properties")

# Display text properties above the camera preview
st.subheader("Text Properties:")
st.write("Here you can add some descriptive text about the camera preview.")

# Use st.camera_input to capture a photo from the webcam
# img_file_buffer = st.camera_input("", label_visibility='hidden')

# if img_file_buffer is not None:
#     # To read image file buffer as a PIL Image:
#     img = Image.open(img_file_buffer)

#     # Display the camera preview
#     st.image(img, caption="Camera Preview", use_column_width=True)

# image = camera_input_live(debounce=33, height=480, width=int(16*480/9))
# st.image(image)
