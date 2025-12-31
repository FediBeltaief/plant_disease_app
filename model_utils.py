import os
# Suppress TF logs for a cleaner terminal
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow as tf
import numpy as np
import cv2

# Use the keras bundled inside tensorflow
from tensorflow.keras.applications.efficientnet import preprocess_input

CLASS_NAMES = [
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_healthy"
]

def build_plant_model(num_classes):
    # Base EfficientNetB0
    base_model = tf.keras.applications.EfficientNetB0(
        include_top=False,
        weights=None, 
        input_shape=(224, 224, 3)
    )
    
    # Rebuilding the exact architecture from your Colab
    model = tf.keras.Sequential([
        base_model,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dropout(0.4),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    return model

print("Loading AI Model...")
MODEL = build_plant_model(len(CLASS_NAMES))

# Load only weights to bypass the Keras 3 Sequential loading bug
try:
    MODEL.load_weights('models/plant_disease_model_final.keras')
    print("AI Model loaded successfully!")
except Exception as e:
    print(f"Error loading weights: {e}")

def predict_disease(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    
    img_array = np.expand_dims(img, axis=0)
    # Correct preprocessing for EfficientNet
    img_array = preprocess_input(img_array)

    predictions = MODEL.predict(img_array, verbose=0)
    class_idx = np.argmax(predictions[0])
    confidence = float(np.max(predictions[0]) * 100)
    
    result = CLASS_NAMES[class_idx]
    
    advice_map = {
        "Early_blight": "Apply fungicides containing chlorothalonil. Improve air circulation.",
        "Late_blight": "Immediate action: Use copper-based fungicides. Destroy infected plants.",
        "healthy": "Your plant is healthy! Continue regular care."
    }
    
    advice = "Monitor plant health. Ensure proper watering."
    for key, val in advice_map.items():
        if key in result:
            advice = val
            
    return result, confidence, advice