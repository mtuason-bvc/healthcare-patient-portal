from flask import Flask, jsonify

app = Flask(__name__)

patients = [
    {"id": 1, "name": "John Doe", "age": 34, "condition": "Diabetes"},
    {"id": 2, "name": "Jane Smith", "age": 45, "condition": "Hypertension"},
]

@app.route('/')
def home():
    return "<h1>Healthcare Organization Patient Portal</h1><p>Welcome to our secure medical record system.</p>"

@app.route('/api/patients', methods=['GET'])
def get_patients():
    return jsonify({"patients": patients})

@app.route('/api/patient/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = next((p for p in patients if p["id"] == patient_id), None)
    if patient:
        return jsonify(patient)
    return jsonify({"message": "Patient not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)