from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)




@app.route('/predict', methods=['POST'])
def add_func():
    pred = request.json.get('num')
    if num > 10:
        return 'too much', 400
    return  jsonify({'prediction': num+1})



if __name__ == '__main__':
    app.run('localhost', 5000)

