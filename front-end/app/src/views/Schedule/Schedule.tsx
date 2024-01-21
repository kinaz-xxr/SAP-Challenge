// Import necessary dependencies
import React, { useCallback, useState } from "react";
import styles from "./Schedule.module.scss";
import DatePicker from "../../components/DatePicker/DatePicker";
import ServicesImpl, { Services } from "../../services/services";
import { useAppContext } from "../../context/AppContext";
import { useSuccessContext } from "../../context/SuccessContext";
import Success from "../../components/Success/Success";
import { useDateContext } from "../../context/DateContext";

const Schedule = () => {
  const { currentDate, setCurrentDate } = useDateContext();

  const { setShowModal } = useAppContext();
  const { setSuccess } = useSuccessContext();

  const services: Services = new ServicesImpl();

  const handleOnPickDate = useCallback(
    async () => {
      services
        .postDate({
          url: "http://127.0.0.1:5000/schedule",
          date: currentDate,
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
    },
    [currentDate, setCurrentDate]
  );

  return (
    <>
      <DatePicker
        onPickDate={handleOnPickDate}
      />
      <Success />
    </>
  );
};

export default Schedule;
