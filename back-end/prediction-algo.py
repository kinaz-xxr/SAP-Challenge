import datetime
import uuid
from models import RevenueLossTable, BayTable1, BayTable2, BayTable3, BayTable4, BayTable5, BayTable6, BayTable7, BayTable8, BayTable9, BayTable10
from app import db, app, AppointmentObject
from sqlalchemy import func

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

def getServiceCharge(carType : str):
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


def predictionAlgo(request):
    # Get the car type
    carType = request.carType

    # Get the date of the start appointment
    dateStartAppointment = request.dateStartAppointment

    # Get the date of the end appointment
    dateEndAppointment = request.dateEndAppointment

    # Get the service charge
    serviceCharge = getServiceCharge(carType)

    decision = inputBay(dateStartAppointment, dateEndAppointment, carType)

    return decision * serviceCharge

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


def lastTable(request : AppointmentObject):
    for table_name in table_names:
        table_class = globals()[table_name]
        query = table_class.query.all()
        print(f"Results for {table_name}:")
    for row in query:
        print(row.dict)
        print("\n")
        return 0


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

def inputBay(appointment : AppointmentObject, table_name):
    selectedTable = TableMap[table_name]
    
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
    allAppointment  = db.session.query(selectedTable).first()
    db.session.delete(allAppointment)
    db.session.commit()
    db.session.close()


def inputRevenueLoss(revenue : int, loss : int, date : str):
    db.session.add(RevenueLossTable(date, revenue, loss))
    db.session.commit()
    db.session.close()
    
with app.app_context():
    appointment = AppointmentObject('9/25/2022 16:01', '11/14/2022 11:25', 'full-size')
    removeLastFromBay('BayTable2')
