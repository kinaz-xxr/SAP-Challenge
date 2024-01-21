from datetime import datetime, timedelta
import uuid
from flask import Flask, request, jsonify
from models import db
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from flask_cors import CORS
from models import RevenueLossTable, BayTable1, BayTable2, BayTable3, BayTable4, BayTable5, BayTable6, BayTable7, BayTable8, BayTable9, BayTable10
from sqlalchemy import func
import uuid
from models import RevenueLossTable, BayTable1, BayTable2, BayTable3, BayTable4, BayTable5, BayTable6, BayTable7, BayTable8, BayTable9, BayTable10
from sqlalchemy import func
import pandas as pd
from models import db
import numpy as np
from datetime import datetime

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
TableMap = {
    'BayTable1': BayTable1, 
    'BayTable2': BayTable2,
    'BayTable3': BayTable3,
    'BayTable4': BayTable4,
    'BayTable5': BayTable5,
    'BayTable6': BayTable6,
    'BayTable7': BayTable7,
    'BayTable8': BayTable8,
    'BayTable9': BayTable9,
    'BayTable10': BayTable10
}
bayToTableMap = {
    'compact':'BayTable1',
    'medium':'BayTable2',
    'full-size':'BayTable3',
    'class 1 truck':'BayTable4',
    'class 2 truck':'BayTable5',
    'bayflex1':'BayTable6',
    'bayflex2':'BayTable7',
    'bayflex3':'BayTable8',
    'bayflex4':'BayTable9',
    'bayflex5':'BayTable10'
}


def inputBay(dateStartAppointment : str, dateEndAppointment : str, carType : str):
    # Assuming the tables were dynamically created with names BayTable1, BayTable2, ..., BayTable10
    table_names = [f'BayTable{i}' for i in range(1, 11)]

    # Create a list to store Table objects for each table name
    tables = []

    if carType == 'compact':
        table_class = globals()['BayTable1']
        # if table is empty, then add the appointment
    elif carType == 'medium':
        table_class = globals()['BayTable2']
    elif carType == 'full-size':
        table_class = globals()['BayTable3']
    elif carType == 'class 1 truck':
        table_class = globals()['BayTable4']
    elif carType == 'class 2 truck':
        table_class = globals()['BayTable5']
    else:
        return
        # If table 6-9 are empty, or if appointment start time is after most recent appointment 
        # end time, then add the appointment and return 1 else return -1

        # If table 6-9 are not empty, then apply algorithm to determine 10th table


def isBayEmpty( appointment : AppointmentObject , table_name: str)->bool:

    selectedTable = TableMap[table_name]
    
    appointmentDate : str = appointment.dateStartAppointment[:10].strip()

    appointmentsOnDate = appointmentsOnDate = db.session.query(selectedTable).filter(
        func.substr(selectedTable.dateStartAppointment, 1, 10) == str(appointmentDate)
    ).all()

    for appointments in appointmentsOnDate:
        appointments.to_dict()
        if (datetime.strptime(appointments.dateEndAppointment, '%m/%d/%Y %H:%M') >= 
            datetime.strptime(appointment.dateEndAppointment, '%m/%d/%Y %H:%M')):
            return False

    return True

def inputBayTable(appointment : AppointmentObject, table_name):
    selectedTable = TableMap[table_name]
    print('in')
    appointmentObject = selectedTable(id=str(uuid.uuid4()), 
                                    dateBooked = appointment.dateBooked, 
                                    dateStartAppointment = appointment.dateStartAppointment, 
                                    dateEndAppointment = appointment.dateEndAppointment, 
                                    carType = appointment.carType
                                    )
    db.session.add(appointmentObject)
    db.session.commit()
    db.session.close()

def removeLastFromBay(table_name):
    selectedTable = TableMap[table_name]  
    allAppointment  = db.session.query(selectedTable).one_or_none()
    db.session.delete(allAppointment)
    db.session.commit()
    db.session.close()


def inputRevenueLoss(revenue : int, loss : int, date : str, compact_loss, medium_loss, full_size_loss, class_1_loss, class_2_loss):
    print('in')
    db.session.add(RevenueLossTable(id = str(uuid.uuid1()),  revenue = revenue, loss=loss, date = date, compact_loss = compact_loss, medium_loss = medium_loss, full_size_loss = full_size_loss, class_1_loss=class_1_loss, class_2_loss=class_2_loss))
    db.session.commit()
    db.session.close()


def getServiceCharge(carType):
    if (carType == 'compact'):
        return 150
    elif(carType == 'medium'):
        return 150
    elif(carType == 'full-size'):
        return 150
    elif(carType == 'class 1 truck'):
        return 250
    elif(carType == 'class 2 truck'):
        return 700


car_service_time = {
    "compact": np.timedelta64(30, 'm'),
    "medium": np.timedelta64(30, 'm'),
    "full-size": np.timedelta64(30, 'm'),
    "class 1 truck": np.timedelta64(60, 'm'),
    "class 2 truck": np.timedelta64(120, 'm')
}

def iterateDay(df):
    date = [x[:10] for x in df["requested appointment"].values]
    df["date"] = date
    
    requested_time = df["requested time"]
    df["requested time"] = [datetime.strptime(time, '%Y-%m-%d %H:%M') for time in requested_time]
    appointment_time = df["requested appointment"]
    df["requested appointment"] = [datetime.strptime(time, '%Y-%m-%d %H:%M') for time in appointment_time]
    
    car_types_values = df["car type"].values
    requested_appointment_values = df["requested appointment"].values
    finished_time = [requested_appointment_values[i] + car_service_time[car_types_values[i]] for i in range(len(requested_appointment_values))]
    df["finished time"] = finished_time
    
    revenueGain_lst = []
    revenueLost_lst = []
    bays_lst = []
    compact_loss_lst = []
    medium_loss_lst = []
    full_size_loss_lst = []
    class_1_loss_lst = []
    class_2_loss_lst = []
    
    for k in range(0,2):
        for i in range(1, 10):
            bays_dict = {
                #car type, requested time, finished time
                "compact": [], 
                "medium": [],
                "full-size": [],
                "class 1 truck": [],
                "class 2 truck": [],
                "bayflex1": [],
                "bayflex2": [],
                "bayflex3": [],
                "bayflex4": [],
                "bayflex5": []
            }
            df_filtered = df[df["date"]=="2022-1"+str(k)+"-0" + str(i)]
            df_filtered = df_filtered.sort_values(by=["requested appointment", "requested time"])
            revenueGain, revenueLost, rejected_lst = iterateRequest(df_filtered, bays_dict)
            revenueGain_lst.append(revenueGain)
            revenueLost_lst.append(revenueLost)
            bays_lst.append(bays_dict)

            compact_loss = 0
            medium_loss = 0
            full_size_loss = 0
            class_1_loss = 0
            class_2_loss = 0
            for car_type in rejected_lst:
                if car_type == "compact":
                    compact_loss -= getServiceCharge(car_type)
                if car_type == "medium":
                    medium_loss -= getServiceCharge(car_type)
                if car_type == "full-size":
                    full_size_loss -= getServiceCharge(car_type)
                if car_type == "class 1 truck":
                    class_1_loss -= getServiceCharge(car_type)
                if car_type == "class 2 truck":
                    class_2_loss -= getServiceCharge(car_type)
                    
            compact_loss_lst.append(compact_loss)
            medium_loss_lst.append(medium_loss)
            full_size_loss_lst.append(full_size_loss)
            class_1_loss_lst.append(class_1_loss)
            class_2_loss_lst.append(class_2_loss)

            # inputRevenueLoss(revenueGain, revenueLost, "2022-1"+str(k)+"-" + str(i), compact_loss, medium_loss, full_size_loss, class_1_loss, class_2_loss)
        
        for i in range(10, 32):
            bays_dict = {
                #car type, requested time, finished time
                "compact": [], 
                "medium": [],
                "full-size": [],
                "class 1 truck": [],
                "class 2 truck": [],
                "bayflex1": [],
                "bayflex2": [],
                "bayflex3": [],
                "bayflex4": [],
                "bayflex5": []
            }
            df_filtered = df[df["date"]=="2022-1"+str(k)+"-" + str(i)]
            df_filtered.sort_values(by=["requested appointment", "requested time"])
            revenueGain, revenueLost, rejected_lst = iterateRequest(df_filtered, bays_dict)
            revenueGain_lst.append(revenueGain)
            revenueLost_lst.append(revenueLost)


            compact_loss = 0
            medium_loss = 0
            full_size_loss = 0
            class_1_loss = 0
            class_2_loss = 0
            for car_type in rejected_lst:
                if car_type == "compact":
                    compact_loss -= getServiceCharge(car_type)
                if car_type == "medium":
                    medium_loss -= getServiceCharge(car_type)
                if car_type == "full-size":
                    full_size_loss -= getServiceCharge(car_type)
                if car_type == "class 1 truck":
                    class_1_loss -= getServiceCharge(car_type)
                if car_type == "class 2 truck":
                    class_2_loss -= getServiceCharge(car_type)
                    
            compact_loss_lst.append(compact_loss)
            medium_loss_lst.append(medium_loss)
            full_size_loss_lst.append(full_size_loss)
            class_1_loss_lst.append(class_1_loss)
            class_2_loss_lst.append(class_2_loss)

            print(compact_loss)
            # inputRevenueLoss(revenueGain, revenueLost, "2022-1"+str(k)+"-" + str(i), compact_loss, medium_loss, full_size_loss, class_1_loss, class_2_loss)

    return revenueGain_lst, revenueLost_lst, bays_lst

        
def inputBay(request, bays_dict, key):
    appointment_time = request[1]
    car_type = request[2]
    request_finished_date = request[4]
    booked_time = request[0]
    if bays_dict[key] == []:
        bays_dict[key].append([car_type, appointment_time, request_finished_date])
        request_input = AppointmentObject(booked_time, str(appointment_time)[:16], car_type)
        inputBayTable(request_input, bayToTableMap[key])
        return 1
    last_finished_time = bays_dict[key][-1][2]
    if appointment_time > last_finished_time:
        bays_dict[key].append([car_type, appointment_time, request_finished_date])
        request_input = AppointmentObject(booked_time, str(appointment_time)[:16], car_type)
        inputBayTable(request_input, bayToTableMap[key])
        return 1
    else:
        return -1



    
def iterateRequest(df, bays_dict):
    requests_lst = df.values
    revenueGain = 0
    revenueLost = 0
    rejected_lst = []
    for i in range(len(requests_lst)):
        request = requests_lst[i]
        car_key = request[2]
        booked_time = request[0]
        appointment_time = request[1]
        decision = inputBay(request, bays_dict, car_key) # check fixed bays
        if decision < 0:
            for j in range(5, 10):
                decision = inputBay(request, bays_dict, list(bays_dict.keys())[j])
                if decision > 0:
                    # request_input = AppointmentObject(booked_time, appointment_time, car_key)
                    # inputBayTable(request_input, bayToTableMap[list(bays_dict.keys())[j]])
                    break
        if decision > 0:
            revenueGain += getServiceCharge(car_key)
        else:
            revenueLost -= getServiceCharge(car_key)
            rejected_lst.append(car_key)
    return revenueGain, revenueLost, rejected_lst
 


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/upload', methods=['POST'])
def predict():
    file = request.files["file"]
    iterateDay(pd.read_csv(file, names=["requested time", "requested appointment", "car type"]))

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

