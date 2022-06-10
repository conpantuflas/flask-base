from flask import Flask, jsonify, request #clase de flask
#app es una instacia con propiedades de flask, una instancia es un objeto de su clase
app = Flask(__name__)

todos = ['make the bad']

@app.route('/', methods=['GET']) #decorador 1.endpoint  2.metodos
def home():     #funcion
    return 'home oage'

@app.route('/todos', methods=['GET'])    
def get_todos():
    return jsonify(todos)

@app.route('/set_todos', methods=['PUT'])    
def set_todos(): 
    todo = request.json.get('todo')
    todos.append(todo)
    return jsonify(todo)   

@app.route('/delete_todo/<int:id>', methods=['DELETE'])    
def delte_todo(id):
    return jsonify(todos)    

if __name__ == "__main__":
    app.run(host="localhost", port="5000")



