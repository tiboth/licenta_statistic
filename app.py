from flask import Flask, request

from controller.StatisiticController import app

# app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
