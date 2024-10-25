import argparse
from flask import Flask, render_template, request, Response
from werkzeug.utils import  send_from_directory
import os



app = Flask(__name__)


@app.route("/")
def admin():
    return render_template('index.html')

@app.route('/')
def scan():
    return render_template('index.html')

@app.route('/Dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/Recipes')
def recipes():
    return render_template('Pages/recipes.html')

@app.route('/About')
def about():
    return render_template('Pages/about.html')
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov9 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=args.port,debug=True) 
