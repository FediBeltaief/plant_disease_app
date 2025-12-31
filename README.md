# 🌿 PlantCare AI – Plant Disease Detection System

**PlantCare AI** is a full-stack web application that enables automated diagnosis of plant leaf diseases using Deep Learning. Users upload images of **Potato** or **Tomato** leaves and receive an instant prediction including the disease name, confidence score, and actionable treatment recommendations.

The system combines a fine-tuned **EfficientNetB0** CNN with a Flask backend, user authentication, and persistent scan history.

---

## 🖼️ Images

### User Interface
![User Interface](https://i.imgur.com/UlR3fMh.png)

### Analysis Result
![Analysis Result](https://i.imgur.com/wqvoAH7.png)

### Scan History
![Scan History](https://i.imgur.com/q9uabok.png)


## 🚀 Features

* **AI-Powered Diagnosis**
  Fine-tuned EfficientNetB0 CNN trained to classify **6 plant health states** with confidence scoring.

* **User Authentication**
  Secure registration and login using Flask-Login, enabling per-user scan tracking.

* **Personal Dashboard**
  View historical scans with uploaded images, prediction results, and timestamps.

* **Actionable Treatment Advice**
  Disease-specific recommendations (chemical and organic treatments).

* **Responsive UI**
  Bootstrap 5-based interface optimized for desktop and mobile.

---

## 🛠️ Tech Stack

### Backend

* Python **3.10.9**
* Flask
* Flask-SQLAlchemy
* Flask-Login

### Deep Learning

* TensorFlow **2.19.0**
* Keras **3**
* EfficientNetB0 (Fine-tuned)
* OpenCV
* NumPy `< 2.0`

### Database

* SQLite (via SQLAlchemy ORM)

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* Jinja2 Templates

---

## 📂 Project Structure

```text
plant_disease_app/
├── app.py                  # Main Flask app (routes, auth, database)
├── model_utils.py          # Model loading & prediction logic
├── models/
│   └── plant_disease_model_final.keras
├── static/
│   └── uploads/            # Stored user-uploaded images
├── templates/
│   ├── base.html           # Global layout
│   ├── index.html          # Upload & prediction page
│   ├── dashboard.html      # User scan history
│   ├── login.html
│   └── register.html
└── requirements.txt        # Project dependencies
```

---

## 📋 Prerequisites

* Python **3.10.x**
* Virtual environment support (`venv`)
* CPU or GPU capable of running TensorFlow

---

## 📥 Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd plant_disease_app
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
.\venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install flask flask-sqlalchemy flask-login \
tensorflow==2.19.0 "numpy<2.0" \
opencv-python==4.10.0.84 Pillow
```

> **Important**
> NumPy is pinned below 2.0 to ensure compatibility with TensorFlow and OpenCV native extensions.

---

### 4. Prepare the Model

Place your trained model file here:

```text
models/plant_disease_model_final.keras
```

The application will automatically load it at runtime.

---

## 🏃 Running the Application

```bash
python app.py
```

Then open your browser at:

```
http://127.0.0.1:5000
```

---

## 🧪 Supported Classes

The model currently supports the following plant health states:

### Potato

* Potato Early Blight
* Potato Late Blight
* Potato Healthy

### Tomato

* Tomato Early Blight
* Tomato Late Blight
* Tomato Healthy

---

## 🧠 Model Details

* **Architecture:** EfficientNetB0
* **Training Strategy:** Transfer Learning + Fine-tuning
* **Input:** RGB leaf images
* **Output:** Softmax probability distribution over 6 classes
* **Inference:** Single-image prediction with confidence score

---

## 🔮 Future Extensions

* **Leaf Segmentation**
  Background removal using OpenCV GrabCut or Mask R-CNN to improve robustness.

* **Expert Connect**
  Automatic forwarding of scan results to agricultural specialists.

* **Multi-Language Support**
  Localized treatment advice (e.g., Arabic, French) for regional farmers.

* **Expanded Crop Support**
  Additional plant species and disease categories.

---

## 📜 License

This project is intended for **educational and research purposes**.
Commercial deployment should include agronomic validation and regulatory review.

---
