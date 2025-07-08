from flask import Flask, request, jsonify, render_template
import joblib
from utils.features import extract_features
from utils.password_generator import generate_strong_password_with_model

app = Flask(__name__)

# Load model dari folder 'model'
model = joblib.load("model/manual_password_model5000baru.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    password = request.form.get('password') or request.json.get('password')
    if not password:
        return jsonify({'error': 'Password required'}), 400
    
    features = extract_features(password)
    strength = model.predict(features)[0]
    
    # Jika form HTML kirim, tampilkan di browser
    if request.form:
        return render_template("index.html", result=strength, password=password)
    
    return jsonify({'strength': strength})

@app.route('/generate', methods=['GET'])
def generate_password():
    try:
        new_password = generate_strong_password_with_model(model)
        if new_password:
            return jsonify({'generated_password': new_password})
        else:
            return jsonify({'error': 'Failed to generate strong password'}), 500
    except Exception as e:
        print("Error in /generate:", e)
        return jsonify({'error': 'Internal server error'}), 500


   


if __name__ == '__main__':
    app.run(debug=True)
