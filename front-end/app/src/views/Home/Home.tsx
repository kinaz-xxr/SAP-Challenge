import UploadFile from "../../components/Upload/UploadFile";
import AboutSection from "../../components/About/AboutSection";
import Schedule from "../../components/Schedule/Schedule";
import styles from "./Home.module.scss"; 

// Home component
const Home = () => {
    return (
        <div className={styles.Home}>
            <AboutSection />
            <UploadFile />
            <Schedule />
        </div>
    );
};

export default Home;