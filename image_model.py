from PIL import Image
import numpy as np

def predict_image(image):
    # Dummy logic (replace with CNN later)
    img = np.array(image)

    avg_color = img.mean()

    if avg_color < 100:
        return "Disease Detected"
    else:
        return "Healthy"
