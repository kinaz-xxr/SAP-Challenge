import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import LoadingContextProvider from "./context/LoadingContext";
import Home from "./views/Home/Home";
import AppContextProvider from "./context/AppContext";
import Schedule from "./components/Schedule/Schedule";
import AboutSection from "./components/About/AboutSection";
import UploadFile from "./components/Upload/UploadFile";
import Modal from "./components/Modal/Modal";

const App = () => {
  return (
    <Router>
      <AppContextProvider>
        <LoadingContextProvider>
          <Routes>
            <Route path="/home" element={
              <Home />
          } />
          <Route path="/schedule" element={<Schedule />} />
          </Routes>
          <Modal />
        </LoadingContextProvider>
      </AppContextProvider>
    </Router>
  );
};

export default App;
