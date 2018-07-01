from flask import Flask
from flask import render_template
from Doctor import Doctor, initializeDoctors
app = Flask(__name__)

doctors = initializeDoctors()

@app.route('/')
def index():
    return render_template('index.html', doctors=doctors)

@app.route('/<doctor>')
def doctor(doctor):
    doctor = doctors[int(doctor)]
    special_docs = []
    for doc in doctors:
        if doc.specialty == doctor.specialty:
            special_docs.append(doc)

    special_docs.sort(key=lambda x: x.rating, reverse=True)
    return render_template('doctor.html', doctor=doctor, doctors=special_docs)

if __name__ == '__main__':
    app.run(host='0.0.0.0')