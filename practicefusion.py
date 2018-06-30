from flask import Flask
from flask import render_template
from Doctor import Doctor
app = Flask(__name__)

@app.route('/')
def index():
    doctor = Doctor(first="Ricky", last="Kuang", spec="Dermatology", area="Alhambra, CA", score=5.0)
    return render_template('index.html', doc=doctor)

if __name__ == '__main__':
    app.run(host='0.0.0.0')