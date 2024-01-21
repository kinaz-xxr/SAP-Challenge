import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import LoadingContextProvider from "./context/LoadingContext";
import Home from "./views/Home/Home";
import Schedule from "./components/Schedule";
import AboutSection from "./components/AboutSection";
import UploadFile from "./components/Upload/UploadFile";

const App = () => {
  return (
    <Router>
      <LoadingContextProvider>
        <Routes>
          <Route path="/home" element={
            <div>
              <Home />
              <UploadFile />
              <AboutSection />
            </div>
          } />
          <Route path="/schedule" element={<Schedule />} />
        </Routes>
      </LoadingContextProvider>
    </Router>
  );
};

export default App;
