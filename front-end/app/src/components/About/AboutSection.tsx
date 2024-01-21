// Import necessary dependencies
import React from "react";
import { useEffect, useState } from "react";
import styles from './AboutSection.module.scss';

// Define the functional component
const AboutSection: React.FC = () => {
    return (
        <div className={styles.UploadFile}>
            <p>Our software optimizes your car washing schedule.</p>
        </div>
    );
}

export default AboutSection;
