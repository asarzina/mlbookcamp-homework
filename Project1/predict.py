import pickle
import xgboost as xgb

from flask import Flask
from flask import request
from flask import jsonify

dv_file = 'dv.bin'
model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as dv_in:
    dv = pickle.load(dv_in)

app = Flask('churn')

@app.route('/heartbit', methods=['GET'])
def heartbit():
    return 'ok'

@app.route('/predict', methods=['POST'])
def predict():
    person = request.get_json()
    print('person', person)

    X_val = dv.transform([person])
    X = xgb.DMatrix(X_val)
    y_pred = model.predict(X)

    result = {
        'income': bool(y_pred)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
