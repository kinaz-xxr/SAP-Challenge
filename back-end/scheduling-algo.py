from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#hi
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
        df_filtered = df[df["date"]=="2022-10-0" + str(i)]
        df_filtered = df_filtered.sort_values(by=["requested appointment", "requested time"])
        revenueGain, revenueLost = iterateRequest(df_filtered, bays_dict)
        revenueGain_lst.append(revenueGain)
        revenueLost_lst.append(revenueLost)
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
        df_filtered = df[df["date"]=="2022-10-" + str(i)]
        df_filtered.sort_values(by=["requested appointment", "requested time"])
        revenueGain, revenueLost = iterateRequest(df_filtered, bays_dict)
        revenueGain_lst.append(revenueGain)
        revenueLost_lst.append(revenueLost)
        bays_lst.append(bays_dict)
    
    return revenueGain_lst, revenueLost_lst, bays_lst

        
def inputBay(request, bays_dict, key):
    appointment_time = request[1]
    car_type = request[2]
    request_finished_date = request[4]
    if bays_dict[key] == []:
#         bays_dict[key].append([car_type, appointment_time, request_finished_date])
        return 1
    last_finished_time = bays_dict[key][-1][2]
    if appointment_time > last_finished_time:
#         bays_dict[key].append([car_type, appointment_time, request_finished_date])
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
        decision = inputBay(request, bays_dict, car_key) # check fixed bays
        if decision < 0:
            for j in range(5, 10):
                decision = inputBay(request, bays_dict, list(bays_dict.keys())[j])
                if decision > 0:
                    break
        if decision > 0:
            revenueGain += getServiceCharge(car_key)
        else:
            revenueLost -= getServiceCharge(car_key)
    return revenueGain, revenueLost
                