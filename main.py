from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
        data = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!' # return 'Hello World' in response

@app.route('/students')
def get_students():
    result = []
    pref = request.args.get('pref') # get the parameter from url
    if pref:
        for student in data: # iterate dataset
          if student['pref'] == pref: # select only the students with a given meal preference
            result.append(student) # add match student to the result
        return jsonify(result) # return filtered set if parameter is supplied
    return jsonify(data)# return student data in response

@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)


@app.route('/stats')
def get_stats():
  chicken = 0
  fish = 0
  veg = 0
  ComputerScienceM = 0
  ComputerScienceS = 0
  InformationTechnologyM = 0
  InformationTechnologyS = 0
  for student in data:
    if student['pref'] == 'Chicken':
      chicken += 1
    elif student['pref'] == 'Fish':
      fish += 1
    else:
      veg += 1
    if student['programme'] == 'Computer Science (Major)':
      ComputerScienceM += 1
    if student['programme'] == 'Computer Science (Special)':
      ComputerScienceS += 1
    if student['programme'] == 'Information Technology (Major)':
      InformationTechnologyM += 1
    if student['programme'] == 'Information Technology (Special)':
      InformationTechnologyS += 1
  return jsonify({
    'Chicken': chicken,
    'Fish': fish,
    'Veg': veg,
    'Computer Science (Major)': ComputerScienceM,
    'Computer Science (Special)': ComputerScienceS,
    'Information Technology (Major)': InformationTechnologyM,
    'Information Technology (Special)': InformationTechnologyS
  })

@app.route('/add/<float:a>/<float:b>', methods=['GET'])
def add(a, b):
  A_result = a + b
  return jsonify(({"operation": "add", "a": a, "b": b, "result": A_result}))

@app.route('/subtract/<float:a>/<float:b>' , methods=['GET'])
def subtract(a, b):
  S_result = a - b
  return jsonify(({"operation": "subtract", "a": a, "b": b, "result": S_result}))

@app.route('/multiply/<float:a>/<float:b>/' , methods=['GET'])
def multiply(a, b):
  M_result = a * b
  return jsonify(({"operation": "multiply", "a": a, "b": b, "result": M_result}))

@app.route('/divide/<float:a>/<float:b>/' , methods=['GET'])
def divide(a, b):
  D_result = a / b
  return jsonify(({"operation": "divide", "a": a, "b": b, "result": D_result}))

app.run(host='0.0.0.0', port=8080)