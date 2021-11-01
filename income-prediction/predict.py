import pickle
import xgboost as xgb

from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('churn')

@app.route('/heartbit', methods=['GET'])
def heartbit():
    return 'ok'

@app.route('/predict', methods=['POST'])
def predict():
    person = request.get_json()
    print('person', person)

    X = dv.transform([person])
    features = model.feature_names
    dval = xgb.DMatrix(X, feature_names=features)
    y_pred = model.predict(dval, ntree_limit=model.best_iteration)

    result = {
        'income_greater_than_50K_probability': float(y_pred)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
