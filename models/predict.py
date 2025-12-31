import tensorflow as tf
import numpy as np
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.preprocessing import image
import os
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'plant_disease_model_final.keras')

IMG_SIZE = (224, 224)

# Load the trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Map index to class name
# Make sure this matches your training class order
CLASS_NAMES = sorted(os.listdir('data/train'))  # or manually: ['Apple___Black_rot', ...]


def predict_image(img_path):
    """Predict disease class for a single image."""
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3, expand_animations=False)
    img = tf.image.resize(img, IMG_SIZE)
    img_array = preprocess_input(tf.expand_dims(img, axis=0))  # Shape: (1, 224, 224, 3)

    preds = model.predict(img_array)
    pred_idx = np.argmax(preds, axis=1)[0]
    pred_class = CLASS_NAMES[pred_idx]
    confidence = float(preds[0][pred_idx])
    
    return pred_class, confidence
