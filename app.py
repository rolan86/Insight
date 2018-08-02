import os

from flask import Flask, render_template, request
from insight import CloudRover


DATA_DIR = os.path.abspath('data')

app = Flask(__name__)

cr = CloudRover()


@app.route('/')
def index():
    #data = open(os.path.join(DATA_DIR, 'ebs.json')).read()
    data = cr.volume_info() 
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
