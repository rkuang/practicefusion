from flask import Flask
from flask import render_template
from Doctor import Doctor, initializeDoctors
app = Flask(__name__)

@app.route('/')
def index():
    doctors = initializeDoctors()
    return render_template('index.html', doctors=doctors)

if __name__ == '__main__':
    app.run(host='0.0.0.0')