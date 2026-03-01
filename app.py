import streamlit as st
from src.ml_logic import extract_aesthetic_palette

st.set_page_config(page_title="AestheteSync AI", page_icon="🎨")

st.title("🎨 AestheteSync: AI Color Analyzer")
st.write("Extract cinematic palettes using Unsupervised Learning (K-Means).")

uploaded_file = st.file_uploader("Upload an Anime Reference", type=['jpg', 'png'])

if uploaded_file:
    # Save temp file
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.image(uploaded_file, caption="Reference Image", width=400)
    
    if st.button("Analyze Aesthetic Palette"):
        with st.spinner("Running K-Means Clustering..."):
            palette = extract_aesthetic_palette("temp.jpg")
            
            st.subheader("Extracted Palette (Centroids)")
            cols = st.columns(len(palette))
            
            for i, color in enumerate(palette):
                # Display the color box
                hex_val = '#%02x%02x%02x' % tuple(color)
                cols[i].markdown(f'<div style="background-color:{hex_val}; height:60px; border-radius:10px;"></div>', unsafe_allow_html=True)
                # Show the RGB values for Premiere
                cols[i].code(f"R: {color[0]}\nG: {color[1]}\nB: {color[2]}")

            st.info("💡 **How to use in Premiere Pro 2022:**\n"
                    "Go to **Lumetri Color > Creative > Shadow Tint** and use the RGB values above to match the 'vibe' of your anime reference!")