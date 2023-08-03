from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello, World!'

todos= [
    { "label": "Walked the dog", "done": True },
    { "label": "Cleaned the house", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop((position-1))
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
