from typing import Counter
from flask import Flask, request, jsonify
from model import McNLP
from flask_cors import CORS
import json
import threading, queue
app = Flask(__name__)
cors = CORS(app)
model = McNLP()

tasks = queue.Queue()
results = {}
class Task:
    def __init__(self,client,string_to_start,temperature=1,max_length=200):
        self.client = client
        self.string_to_start = string_to_start
        self.temperature = temperature
        self.max_length = max_length
    def generate(self, model):
        return model.generate(self.string_to_start,self.temperature,self.max_length).replace('<s>','')

def worker():
    while True:
        item = tasks.get()
        print(f'Working on {item.client} req')
        res = item.generate(model)
        results[item.client] = res
        print(f'Finished {item.client} req')
        tasks.task_done()


count = 0
@app.route('/generate', methods=['POST'])
def generate():
    global count
    
    # Retrieve the name from url parameter
    print("got generate from:")
    print(request.remote_addr)
    string_to_start = request.json.get("string_to_start", None)
    count += 1
    try:
        temperature = float(request.json.get("temperature"))
        max_length = int(request.json.get("max_length"))
        print(temperature)
        print(max_length)
        
        tasks.put(Task(count,string_to_start,temperature,max_length))
    except Exception as identifier:
        tasks.put(Task(count,string_to_start))
    
    # For debugging
    
    return json.dumps({'id':count}), 200

@app.route('/getres', methods=['GET'])
def get_result():
    print("got get from:")
    print(request.args.get('id'))
    if int(request.args.get('id')) in results:
        rap = results[int(request.args.get('id'))]
        
        del results[int(request.args.get('id'))]
        print("ready")
        return json.dumps({'ready':True,'rap':rap}), 200
    else:
        print("not ready")
        return json.dumps({'ready':False})
    
    # Return the response in json format

threading.Thread(target=worker, daemon=True).start()
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    
    app.run(threaded=True, port=5000)