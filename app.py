from flask import Flask, request, jsonify
from model import McNLP
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)
model = McNLP()
@app.route('/generate', methods=['GET'])
def generate():
    # Retrieve the name from url parameter
    string_to_start = request.args.get("string_to_start", None)
    try:
        temperature = float(request.args.get("temperature"))
        max_length = int(request.args.get("max_length"))
        print(temperature)
        print(max_length)
        generated =  model.generate(string_to_start,temperature,max_length)
    except Exception as identifier:
        generated =  model.generate(string_to_start)
    
    # For debugging
    

    response = {'rap':generated.replace('<s>','')}

    
    # Return the response in json format
    return jsonify(response)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)