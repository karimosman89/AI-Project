from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model
model = joblib.load('model/model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
