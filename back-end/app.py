import datetime
import uuid
from flask import Flask, request
from models import db
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'cockroachdb://dat:a8yS_VjWUTTMdhfXLQ70Cw@waning-reptile-6926.g8z.gcp-us-east1.cockroachlabs.cloud:26257/defaultdb'
db.init_app(app)
CORS(app)  # Enable CORS for all routes

def getFixTime(carType : str):
    if (carType == 'compact'):
        return 30
    elif(carType == 'medium'):
        return 30
    elif(carType == 'full-size'):
        return 30
    elif(carType == 'class 1 truck'):
        return 60
    elif(carType == 'class 2 truck'):
        return 120


class AppointmentObject:
    def __init__(self, id : str, dateBooked : str, dateStartAppointment : str, carType : str):
        self.id = id 
        self.dateBooked = dateBooked
        self.dateStartAppointment = dateStartAppointment
        self.dateEndAppointment = datetime.strptime(dateStartAppointment, '%m/%d/%Y %I:%M:%S %p') + datetime.timedelta(minutes=getFixTime(carType))
        self.carType = carType
with app.app_context():
    db.create_all()


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/upload', methods=['POST'])
def predict():
    file = request.files["file"]
    print(pd.read_csv(file))
    # loAppointmentObject : list[AppointmentObject] = request.form.get('table')
    # for appointment in loAppointmentObject:
    #     appointmentObject = AppointmentObject(  str(uuid.uuid1()), 
    #                                             appointment.dateBooked, 
    #                                             appointment.dateStartAppointment, 
    #                                             appointment.dateEndPAppointment, 
    #                                             appointment.carType)

        ##Update Database

        ## if new date get new lambda 

lambda_object = {
    'compact': 2048/(24*60), 
    'medium': 2037/(24*60), 
    'full-size': 2005/(24*60), 
    'class-1':1982/(24*60), 

}
  # Create tables when the app starts
