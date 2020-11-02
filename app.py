from flask import Flask, request, jsonify
from model import McNLP
app = Flask(__name__)
model = McNLP()
@app.route('/generate', methods=['GET'])
def generate():
    # Retrieve the name from url parameter
    string_to_start = request.args.get("string_to_start", None)
    temperature = request.args.get("temperature")
    max_length = request.args.get("max_length")
    # For debugging
    generated =  model.generate(string_to_start)

    response = {'rap':generated}

    
    # Return the response in json format
    return jsonify(response)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)