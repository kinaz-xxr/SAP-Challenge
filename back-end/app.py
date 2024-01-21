from datetime import datetime, timedelta
import uuid
from flask import Flask, request, jsonify
from models import db
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from flask_cors import CORS
from models import RevenueLossTable, BayTable1, BayTable2, BayTable3, BayTable4, BayTable5, BayTable6, BayTable7, BayTable8, BayTable9, BayTable10
from sqlalchemy import func
from prediction_algo import iterateDay

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
    def __init__(self,  dateBooked : str, dateStartAppointment : str, carType : str):
        self.id = str(uuid.uuid1())
        self.dateBooked = dateBooked
        self.dateStartAppointment = dateStartAppointment
        self.dateEndAppointment = datetime.strptime(dateStartAppointment, '%Y-%m-%d %H:%M') + timedelta(minutes=getFixTime(carType))
        self.carType = carType



@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/upload', methods=['POST'])
def predict():
    file = request.files["file"]
    print(pd.read_csv(file))
    iterateDay(pd.read_csv(file))
    
@app.route('/schedule', methods=['POSTS'])
def schedule():
    date = request.form.get('table')
    table_1 = db.session.query(BayTable1).filter(
        func.substr(BayTable1.dateStartAppointment, 1, 10) == str(date)
    ).all().as_dict()

    table_1_dict = {row.as_dict()["id"]:row.as_dict() for row in table_1}

    table_2 = db.session.query(BayTable2).filter(
        func.substr(BayTable2.dateStartAppointment, 1, 10) == str(date)
    ).all()

    table_2_dict = {row.as_dict()["id"]:row.as_dict() for row in table_2}

    table_3 = db.session.query(BayTable3).filter(
        func.substr(BayTable3.dateStartAppointment, 1, 10) == str(date)
    ).all()

    table_3_dict = {row.as_dict()["id"]:row.as_dict() for row in table_3}

    table_4 = db.session.query(BayTable4).filter(
        func.substr(BayTable4.dateStartAppointment, 1, 10) == str(date)
    ).all()

    table_4_dict = {row.as_dict()["id"]:row.as_dict() for row in table_4}

    table_5 = db.session.query(BayTable5).filter(
        func.substr(BayTable5.dateStartAppointment, 1, 10) == str(date)
    ).all()

    table_5_dict = {row.as_dict()["id"]:row.as_dict() for row in table_5}

    table_6 = db.session.query(BayTable6).filter(
        func.substr(BayTable6.dateStartAppointment, 1, 10) == str(date)
    ).all()

    table_6_dict = {row.as_dict()["id"]:row.as_dict() for row in table_6}

    table_7 = db.session.query(BayTable7).filter(
        func.substr(BayTable7.dateStartAppointment, 1, 10) == str(date)
    ).all()

    table_7_dict = {row.as_dict()["id"]:row.as_dict() for row in table_7}

    table_8 = db.session.query(BayTable8).filter(
        func.substr(BayTable8.dateStartAppointment, 1, 10) == str(date)
    ).all()

    table_8_dict = {row.as_dict()["id"]:row.as_dict() for row in table_8}

    table_9 = db.session.query(BayTable9).filter(
        func.substr(BayTable9.dateStartAppointment, 1, 10) == str(date)
    ).all()

    table_9_dict = {row.as_dict()["id"]:row.as_dict() for row in table_9}

    table_10 = db.session.query(BayTable10).filter(
        func.substr(BayTable10.dateStartAppointment, 1, 10) == str(date)
    ).all()

    table_10_dict = {row.as_dict()["id"]:row.as_dict() for row in table_10}


    return jsonify(
        {
            'table-1': table_1_dict, 
            'table-2': table_2_dict, 
            'table-3': table_3_dict, 
            'table-4': table_4_dict, 
            'table-5': table_5_dict, 
            'table-6': table_6_dict, 
            'table-7': table_7_dict, 
            'table-8': table_8_dict,
            'table-9': table_9_dict,
            'table_10': table_10_dict
        }

    )
