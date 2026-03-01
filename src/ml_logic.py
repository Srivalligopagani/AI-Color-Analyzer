import cv2
import numpy as np
from sklearn.cluster import KMeans

def extract_aesthetic_palette(img_path, k=5):
    # Load image and convert to RGB
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Preprocessing: Resize and flatten for the ML model
    img = cv2.resize(img, (200, 200))
    pixels = img.reshape(-1, 3)
    
    # The ML Algorithm: K-Means Clustering
    model = KMeans(n_clusters=k, n_init=10)
    model.fit(pixels)
    
    # Return the central colors (Centroids)
    return model.cluster_centers_.astype(int)