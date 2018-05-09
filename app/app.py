from flask import Flask

app = Flask('__name__')

@app.route('/auth/login', methods=('POST'))
def index():
    pass

@app.route('/auth/signup', methods=('POST'))
def signup():
    pass

@app.route('/meals/', methods=('GET'))
def getMeal():
    pass

@app.route('/meals/', methods=('POST'))
def addMeal():
    pass

@app.route('/meals/<mealId>', methods=('PUT'))
def updateMealinfo():
    pass

@app.route('/meals/<mealId>', methods=('DELETE'))
def removeMeal():
    pass

@app.route('/menu/', methods=('POST'))
def menu():
    pass

@app.route('/menu/', methods=('GET'))
def custMenu():
    pass

@app.route('/orders', methods='POST')
def orders():
    pass

@app.route('/orders/orderId', methods='PUT')
def orderModify():
    pass

@app.route('/orders', methods='GET')
def orderGet():
    pass