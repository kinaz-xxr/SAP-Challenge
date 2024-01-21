// Import necessary dependencies
import React from "react";
import { useEffect, useState } from "react";
import styles from './AboutSection.module.scss';

// Define the functional component
const AboutSection: React.FC = () => {
    return (
        <>
            <div className={styles.title_text}>
                <p>Optimize Your Revenue</p>
            </div>
            <div className={styles.description}>
                <p>Do you want to maximize your revenue from our car-washing business? We are here with state-of-the-art technology, using advanced algorithm to schedule your bookings with the aim to maximize revenue.</p>
            </div>
            <div className={styles.steps}>
                <div className="step-items">Step 1. Upload your bookings</div>
                <div className="step-items">Step 2. Check your schedule</div>
                <div className="step-items">Step 3. Watch your revenue goes up!</div>
            </div>
        </>
    );
}

export default AboutSection;
