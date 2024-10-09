import os
import uuid
from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model  # Correct import for loading the model

# Configuration du serveur Flask
app = Flask(__name__)
BASE_UPLOAD_FOLDER = 'detection'
os.makedirs(BASE_UPLOAD_FOLDER, exist_ok=True)

# Charger le modèle de machine learning
def load_model_func():
    model = load_model('CNN.h5')  # Load the model using tensorflow.keras.models.load_model
    return model

model = load_model_func()

# Map des classes de tumeurs
tumor_classes = {
    0: 'glioma',
    1: 'meningioma',
    2: 'notumor',
    3: 'pituitary'
}

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image uploaded'}), 400

    try:
        # Générer un nom de fichier unique pour éviter les doublons
        filename = str(uuid.uuid4()) + "_" + file.filename

        img = Image.open(file.stream)
        
        img = img.resize((224, 224))  # Redimensionner selon les besoins de votre modèle
        img_array = np.array(img)

        # Normaliser ou prétraiter l'image selon les besoins de votre modèle
        img_array = img_array / 255.0
        img_array = img_array.reshape((1,224, 224, 3))
        img_array = np.expand_dims(img ,axis=0)  # Add batch dimension
        # Effectuer la prédiction
        prediction = model.predict(img_array)

        result_index = np.argmax(prediction, axis=1)[0]
        print(result_index)
        result_label = tumor_classes.get(result_index, 'unknown')

        # Créer un sous-dossier pour le type de tumeur s'il n'existe pas
        tumor_folder = os.path.join(BASE_UPLOAD_FOLDER, result_label)
        os.makedirs(tumor_folder, exist_ok=True)

        # Enregistrer l'image avec le nom basé sur la prédiction
        image_path = os.path.join(tumor_folder, filename)
        img.save(image_path)

        response = jsonify({'detection': result_label})
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Démarrer le serveur Flask sur l'adresse locale
    app.run(debug=True, host='0.0.0.0', port=5000)
