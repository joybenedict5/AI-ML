from flask import Flask, request, jsonify
from model_inference import predict
from llm_explainer import explain_decision

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_loan():
    data = request.get_json()

    required = ['income', 'credit_score', 'debt_to_income', 'loan_amount', 'employment_years']
    for field in required:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    result      = predict(data)
    explanation = explain_decision(result)
    result["explanation"] = explanation

    return jsonify(result), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "running"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)