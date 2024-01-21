import uuid
from models import RevenueLossTable, BayTable1, BayTable2, BayTable3, BayTable4, BayTable5, BayTable6, BayTable7, BayTable8, BayTable9, BayTable10
from app import app, AppointmentObject
from sqlalchemy import func
import pandas as pd
from models import db
import numpy as np
from datetime import datetime

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


def inputRevenueLoss(revenue : int, loss : int, date : str):
    print('in')
    db.session.add(RevenueLossTable( revenue = revenue, loss=loss, date = date))
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
            revenueGain, revenueLost = iterateRequest(df_filtered, bays_dict)
            revenueGain_lst.append(revenueGain)
            revenueLost_lst.append(revenueLost)
            inputRevenueLoss(revenueGain, revenueLost, "2022-1"+str(k)+"-" + str(i))
            bays_lst.append(bays_dict)
        
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
            revenueGain, revenueLost = iterateRequest(df_filtered, bays_dict)
            revenueGain_lst.append(revenueGain)
            revenueLost_lst.append(revenueLost)
            inputRevenueLoss(revenueGain, revenueLost, "2022-1"+str(k)+"-" + str(i))
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
    return revenueGain, revenueLost
 
with app.app_context():
    iterateDay(pd.read_csv("/datafile (1).csv", names=["requested time", "requested appointment", "car type"]))   
