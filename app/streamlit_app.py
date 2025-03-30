import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import cv2
from utils import process_image, save_image, convert_to_bytes, get_image_metadata

def main():
    st.title("OCT Image Analysis Application")
    st.write("Upload one or multiple OCT images to process and analyze.")

    # Upload Multiple Images
    uploaded_files = st.file_uploader("Choose OCT images...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

    if uploaded_files:
        total_images = len(uploaded_files)
        total_width, total_height, total_channels = 0, 0, 0
        formats = set()

        all_metadata = []
        
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            img_array = np.array(image)

            # Extract metadata
            metadata = get_image_metadata(image, img_array)
            all_metadata.append(metadata)

            # Collect total image statistics
            total_width += image.width
            total_height += image.height
            total_channels += img_array.shape[2] if len(img_array.shape) == 3 else 1
            formats.add(image.format)

        # Display Total Metadata at the Top
        st.markdown("## Total Image Information")
        total_info = pd.DataFrame({
            "Total Images": [total_images],
            "Avg Width": [total_width // total_images],
            "Avg Height": [total_height // total_images],
            "Avg Channels": [total_channels // total_images],
            "Formats": [", ".join(formats)]
        })
        st.table(total_info)

        for idx, uploaded_file in enumerate(uploaded_files):
            st.subheader(f"Processing: {uploaded_file.name}")

            image = Image.open(uploaded_file)
            img_array = np.array(image)

            # Display Metadata as a Table
            st.markdown("**Image Information:**")
            st.table(all_metadata[idx])

            # Display Original Image
            st.image(image, caption="Uploaded OCT Image", use_container_width=True)

            # User controls for edge detection
            st.sidebar.header(f"Processing Settings for {uploaded_file.name}")
            canny_threshold1 = st.sidebar.slider(f"Canny Threshold 1 ({uploaded_file.name})", 0, 255, 50)
            canny_threshold2 = st.sidebar.slider(f"Canny Threshold 2 ({uploaded_file.name})", 0, 255, 150)

            # Process image
            gray, equalized, blurred, edges, adaptive_thresh = process_image(img_array, canny_threshold1, canny_threshold2)

            # Display Processed Images in a Grid Layout (Reduced Size)
            st.markdown("### Processed Images")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.image(gray, caption="Grayscale", width=200, clamp=True)
                st.image(blurred, caption="Gaussian Blur", width=200, clamp=True)

            with col2:
                st.image(equalized, caption="Histogram Equalization", width=200, clamp=True)
                st.image(edges, caption="Edge Detection", width=200, clamp=True)

            with col3:
                st.image(adaptive_thresh, caption="Adaptive Thresholding", width=200, clamp=True)

            # Save Processed Image and Provide Download
            if st.button(f"Generate Download for {uploaded_file.name}"):
                processed_path = save_image(edges, f"processed_{uploaded_file.name}")
                st.download_button(
                    label="Download Processed Image",
                    data=convert_to_bytes(processed_path),
                    file_name=f"processed_{uploaded_file.name}",
                    key=f"download_{uploaded_file.name}"
                )

if __name__ == "__main__":
    main()
