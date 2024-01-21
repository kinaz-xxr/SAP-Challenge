from flask import request, jsonify, Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import uuid
from sqlalchemy import select

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



class BaseTable(db.Model):
    __abstract__ = True

    id = db.Column(db.String(100), primary_key=True)
    dateBooked = db.Column(db.String(40))
    dateStartAppointment = db.Column(db.String(40))
    dateEndAppointment = db.Column(db.String(40))
    carType = db.Column(db.String(40))

# Create 10 tables with names BayTable1, BayTable2, ..., BayTable10
for i in range(1, 11):
    table_name = f'BayTable{i}'

    # Define a class dynamically with the desired table name and inherit from BaseTable
    class_name = f'BayTable{i}'
    table_class = type(class_name, (BaseTable,), {'__tablename__': table_name})
    
    # Add the class to the global namespace (optional)
    globals()[class_name] = table_class
    


# Assuming the tables were dynamically created with names BayTable1, BayTable2, ..., BayTable10
table_names = [f'BayTable{i}' for i in range(1, 11)]

# Create a list to store Table objects for each table name
tables = []

# Query each table and print the results
with app.app_context():
    for i in range(1, 11):
        table_name = f'BayTable{i}'
        table_class = globals().get(table_name)

        if table_class:
            query = table_class.query.all()
            print(f"Results for {table_name}:")
            for row in query:
                print(row.__dict__)
            print("\n")


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
