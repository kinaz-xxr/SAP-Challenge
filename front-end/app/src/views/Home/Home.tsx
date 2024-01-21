import UploadFile from "../Upload/UploadFile";
import AboutSection from "../../components/About/AboutSection";
import Schedule from "../Schedule/Schedule";
import Description from "../../components/Description/Description";
import styles from "./Home.module.scss";

// Home component
const Home = () => {
  return (
    <div className={styles.Home}>
      <AboutSection />
      <Description />
    </div>
  );
};

export default Home;
