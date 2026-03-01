# 🎬 AestheteSync: AI-Driven Cinematic Color Extraction

**AestheteSync** is a Machine Learning tool that uses **Unsupervised Learning** to analyze and extract dominant color palettes from cinematic and anime imagery. This project bridges the gap between Computer Vision and Creative Design, allowing editors to quantify the "vibe" of a reference frame.

---

## 💡 The Innovation
Manual color matching is subjective and time-consuming. AestheteSync uses **K-Means Clustering** to mathematically identify the most significant color manifolds in an image, providing precise RGB and HEX values for professional color grading.

## 🛠️ Technical Stack
- **Machine Learning:** Scikit-learn (K-Means Clustering)
- **Computer Vision:** OpenCV (Image Preprocessing & Colorspace Conversion)
- **Web Interface:** Streamlit
- **Languages:** Python 3.9+

---

## 📂 Project Structure
- `app.py`: The interactive Streamlit dashboard.
- `src/ml_logic.py`: The core ML pipeline (Preprocessing -> Clustering -> Centroid Extraction).
- `data/`: Sample cinematic reference frames (e.g., Sunset Anime scenes).

---

## 🧠 Machine Learning Approach: K-Means
In this project, every pixel is treated as a data point in a 3D coordinate system (R, G, B). 
1. **Initialization:** 5 random centroids are placed in the color space.
2. **Assignment:** Every pixel is assigned to the nearest centroid based on Euclidean distance.
3. **Update:** Centroids move to the average center of their assigned pixels.
4. **Convergence:** The final 5 centroids represent the "Aesthetic Palette" of the image.

---

## 🚀 How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Launch the app: `streamlit run app.py`
4. Upload your favorite anime screenshot and extract the "vibe"!