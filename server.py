# Import Flask to allow us to create our app
from flask import Flask

# Create a new instance of the Flask class called "app"
app = Flask(__name__)

# Create a route that responds with "Hello World!"
@app.route('/')
def hello_world():
    return 'Hello World!'

# Create a route that responds with "Dojo!"
@app.route('/dojo')
def success():
    return "Dojo!"

# Create a route that responds with "Hi" and whatever name is in the URL after /say/
@app.route('/say/<string:name>')
def hello(name):
    print(name)
    return "Hi, " + name

# Create a route that responds with the given word repeated as many times as specified in the URL
@app.route('/repeat/<int:number>/<string:word>')
def repeat(number, word):
    return f"{number * word}"

# SENSEI BONUS: Ensure that if the user types in any route other than the ones specified,
# they receive an error message saying "Sorry! No response. Try again."


# Ensure this file is being run directly and not from a different module
if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8000)