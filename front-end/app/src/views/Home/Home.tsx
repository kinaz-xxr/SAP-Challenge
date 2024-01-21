import UploadFile from "../../components/Upload/UploadFile";
import AboutSection from "../../components/About/AboutSection";
import Schedule from "../Schedule/Schedule";
import styles from "./Home.module.scss";

// Home component
const Home = () => {
  return (
    <div className={styles.Home}>
      <AboutSection />
    </div>
  );
};

export default Home;
