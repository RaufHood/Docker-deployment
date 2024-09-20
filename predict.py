import pickle
from flask import Flask, request, jsonify

with open('./model_C=1.0.bin', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)


app = Flask('churn')

# endpoint in which adress the function leaves
@app.route('/predict', methods=['POST'])
def  predict():
    customer = request.get_json()
    X = dv.transform(customer)
    y_pred = float(model.predict_proba(X)[0,1])
    churn = bool(y_pred >0.5)
    result = {
        'churn_probability': y_pred,
        'churn': churn
        }
    
    return jsonify(result)

if __name__ == '__main__':
    # if bug automatically resutart
    app.run(debug=True, host ='0.0.0.0', port=9696)

