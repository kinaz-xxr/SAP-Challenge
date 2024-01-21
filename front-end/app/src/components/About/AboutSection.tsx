// Import necessary dependencies
import React from "react";
import { useEffect, useState } from "react";
import styles from './AboutSection.module.scss';
import Button from "../Button/Button";
import { useAppContext } from "../../context/AppContext";
import UploadFile from "../Upload/UploadFile";
import { useLoadingContext } from "../../context/LoadingContext";
import Loading from "../Loading/Loading";

// Define the functional component
const AboutSection: React.FC = () => {
    const { setModalContent, setShowModal } = useAppContext();
    const { setLoading } = useLoadingContext();

    return ( 
        <>
            <div className={styles.title_text}>
                <p>Optimize Your Revenue</p>
            </div>
            <div className={styles.description}>
                <p>Do you want to maximize your revenue from our car-washing business? We are here with state-of-the-art technology, using advanced algorithm to schedule your bookings with the aim to maximize revenue.</p>
            </div>
            <div className={styles.steps}>
                <Button 
                    label="Step 1. "
                    onClick={() => {
                        setShowModal(true);
                        setLoading(true);
                        setModalContent(<Loading />);
                        setTimeout(() => {
                            setLoading(false);
                            setModalContent(<UploadFile />);
                            console.log("Here");
                        }, 2000);
                    }}
                />
                <div className="step-items">Step 2. Check your schedule</div>
                <div className="step-items">Step 3. Watch your revenue goes up!</div>
            </div>
            <Loading />
        </>
    );
}

export default AboutSection;