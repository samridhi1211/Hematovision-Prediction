🧬 HematoVision: Blood Cell Classification System

🔍 Overview HematoVision is a deep learning-based web application that classifies blood cell images into four categories using Transfer Learning. The model is deployed using Flask, allowing users to upload an image and get real-time predictions.

🚀 Features

📤 Upload blood cell images via web interface

🤖 Deep Learning model (MobileNetV2)

🎯 Real-time prediction

📊 Confidence score display

🖼️ Image preview before prediction

🌐 Flask-based deployment
🧠 Model Details

 Architecture: MobileNetV2 (Transfer Learning)
 
 Input Size: 224 × 224
 
 Classes:
       Eosinophil
       Lymphocyte
       Monocyte
       Neutrophil
       
 Training Accuracy: ~80%
🛠️ Tech Stack

Python

TensorFlow / Keras

Flask

HTML / CSS / JavaScript
📁 Project Structure

│Hematovision/ ├── app.py # Flask application ├── train.py # Model training script ├── check_data.py # Dataset verification ├── model.h5 # Trained model (ignored in GitHub) │ ├── templates/ │ └── index.html # UI │ ├── static/ │ └── uploads/ # Uploaded images │ ├── dataset/ # Dataset (ignored) ├── .gitignore └── README.md

▶️ How to Run the Project

1️⃣ Clone Repository git clone https://github.com/samridhi1211/Hematovision-Blood-Cell-Test.git cd Hematovision-Blood-Cell-Test

2️⃣ Setup Environment conda create -n hemato python=3.10 conda activate hemato

3️⃣ Install Dependencies pip install numpy pandas matplotlib seaborn scikit-learn tensorflow flask pillow

4️⃣ Run Application python app.py

5️⃣ Open in Browser http://127.0.0.1:5000/

📸 Demo 👉 Upload an image → Click Predict → View result

Screenshot 2026-03-27 233909
About
No description, website, or topics provided.
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 0 watching
Forks
 0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
1
@samridhi1211
samridhi1211 samridhi gupta
Languages
Python
63.2%
 
HTML
36.8%
Suggested workflows
Based on your tech stack
SLSA Generic generator logo
SLSA Generic generator
Generate SLSA3 provenance for your existing release workflows
Pylint logo
Pylint
Lint a Python application with pylint.
Python Package using Anaconda logo
Python Package using Anaconda
Create and test a Python package on multiple Python versions using Anaconda for package management.
More workflows
Footer
