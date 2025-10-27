"""
Idress Baguaei 
Oct, 27 2025
Lab 12, Intro to Flask 
"""
from flask import Flask, render_template, url_for

"""
create an object "app" from flask module
__name__ set to __main__ if the script is running directly to the main file 
"""
app = Flask(__name__)

# Set the routing to the main page 
# routedecorator is used to access the root URL
@ app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return '<h1>About us</h1>'

@app.route('/quotes')
def quotes():
    return '<h1>Quotes</h1>'

# set the app to run if you execute the file directly (not when its imported)
if __name__ == "__main__":
    app.run(debug=True)