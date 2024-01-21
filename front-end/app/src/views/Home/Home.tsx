import UploadFile from "../../components/Upload/UploadFile";
import AboutSection from "../../components/AboutSection";
import Schedule from "../../components/Schedule";

// Home component
const Home = () => {
    return (
        <div>
            <AboutSection />
            <UploadFile />
            <Schedule />
        </div>
    );
};

export default Home;