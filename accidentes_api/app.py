# Dependencies
from flask import Flask, request, jsonify
import traceback
import pickle
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if model:
        try:
            json_ = request.json
            print(json_)
            query = pd.DataFrame(json_)
            print(query)
            

            prediction = list(model.predict(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = '3306' # If you don't provide any port the port will be set to 12345

    model = pickle.load(open('model.pkl', 'rb'))
    print ('Model loaded')

    app.run(host='0.0.0.0', port=port)