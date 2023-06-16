from flask import Flask,jsonify
from pathlib import Path
import os
import subprocess

# Create the Flask app
app = Flask(__name__)

# Define the API endpoint
@app.route('/api/modifyRecepie', methods=['GET'])
def show():
    result = subprocess.check_output(['python','ex5.py'])
    return result.decode('utf-8')

# Run the Flask app 
if __name__ == '__main__':
    app.run()
