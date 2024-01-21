// Import necessary dependencies
import React, { useCallback, useState } from "react";
import styles from './Schedule.module.scss';
import DatePicker, { DatePickerData, defaultDatePickerData } from "../../components/DatePicker/DatePicker";
import ServicesImpl, { Services } from "../../services/services";
import { useAppContext } from "../../context/AppContext";
import { useSuccessContext } from "../../context/SuccessContext";


const Schedule = () => {
    const [datePickerData, setDatePickerData] = React.useState<DatePickerData>({
        ...defaultDatePickerData
    });

    const { setShowModal } = useAppContext();
    const { setSuccess } = useSuccessContext();

    const services: Services = new ServicesImpl();


    const handleOnPickDate = useCallback(async (e: any) => {
        e.preventDefault();
        services.postDate({
            url: "http://127.0.0.1:5000/schedule",
            date: datePickerData
        })
        .then((response) => {
            setSuccess(true);
            setTimeout(() => {
                setSuccess(false);
                setShowModal(false);
            }, 2000);
        })
        .catch((error) => {
            throw new Error(`Error with pick date: ${error}`);
        });
    }, [datePickerData, setDatePickerData, defaultDatePickerData]);

    return (
        <DatePicker 
            currentDate={datePickerData}
            setCurrentDate={setDatePickerData}
            onPickDate={handleOnPickDate}
        />
    );
}

export default Schedule;
