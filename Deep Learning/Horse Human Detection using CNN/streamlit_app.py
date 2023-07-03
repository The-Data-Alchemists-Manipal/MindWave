import streamlit as st
import numpy as np
from keras.models import load_model
import keras.utils as image


# Load the saved model
model = load_model('my_model.h5')

# Set custom styles with CSS
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .upload {
        margin-bottom: 20px;
    }
    .result {
        margin-top: 30px;
        font-size: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define the Streamlit app
def main():
    st.title("Image Classification")
    st.markdown("<p class='title'>Image Classification</p>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"], key='file_uploader')

    if uploaded_file is not None:
        # Load and preprocess the uploaded image
        img = image.load_img(uploaded_file, target_size=(300, 300))
        st.image(img, caption="Uploaded Image", use_column_width=True)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        # Perform the image classification
        classes = model.predict(x, batch_size=10)

        # Print the result
        if classes[0] > 0.5:
            st.markdown("<p class='result'>This is a human.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='result'>This is a horse.</p>", unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == '__main__':
    main()
