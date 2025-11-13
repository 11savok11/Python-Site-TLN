from flask import Flask 
from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "Привет"




if __name__ == "__main__":
    app.run(debug=True)
