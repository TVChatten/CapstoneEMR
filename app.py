from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Patient(db.Model):
    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))

@app.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    new_patient = Patient(
        name=data['name'],
        dob=data['dob'],
        address=data.get('address'),
        phone=data.get('phone')
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'Patient created successfully'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)