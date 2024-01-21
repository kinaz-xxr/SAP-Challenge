from flask import request, jsonify, Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import uuid


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'cockroachdb://dat:a8yS_VjWUTTMdhfXLQ70Cw@waning-reptile-6926.g8z.gcp-us-east1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full'
db = SQLAlchemy(app)
Base = declarative_base()

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
        self.dateEndAppointment = datetime.strptime(dateStartAppointment, '%m/%d/%Y %I:%M:%S %p') + timedelta(minutes=getFixTime(carType))
        self.carType = carType



class BayTable(Base): 
    __tablename__ = 'BayTable-1'
    id = db.Column(db.String(100), primary_key = True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))
        

    
with app.app_context():
    # print('run')
    # db.engine.dialect.server_version_info = (23, 1, 14)
    # db.create_all()
    # test_data_object = AppointmentObject(str(uuid.uuid1()), '10/20/2022  6:30:00 PM', '11/23/2022  9:21:00 AM', 'compact')
    # for i in range(1, 11):
    #     BayTableCreator(f'BayTable-{i}')

    # # test_data = BayTable(id = test_data_object.id, 
    # #                     dateBooked = test_data_object.dateBooked, 
    # #                     dateStartAppointment = test_data_object.dateStartAppointment, 
    # #                     dateEndAppointment = test_data_object.dateEndAppointment, 
    # #                     carType = test_data_object.carType)
    # # db.session.add(test_data)
    # db.session.commit()
    table_dict = {}
    for i in range(1,11):   # Create
        table_name = "BayTable" + str(i)
        table_dict[table_name] = BayTable(table_name)



@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/predict', methods=['POST'])
def predict():
    loAppointmentObject : list[AppointmentObject] = request.form.get('table')
    for appointment in loAppointmentObject:
        appointmentObject = AppointmentObject(  str(uuid.uuid1()), 
                                                appointment.dateBooked, 
                                                appointment.dateStartAppointment, 
                                                appointment.dateEndPAppointment, 
                                                appointment.carType)

        ##Update Database

        ## if new date get new lambda 

        print()
lambda_object = {
    'compact': 2048/(24*60), 
    'medium': 2037/(24*60), 
    'full-size': 2005/(24*60), 
    'class-1':1982/(24*60), 

}
