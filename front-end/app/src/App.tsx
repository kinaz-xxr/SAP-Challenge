import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import LoadingContextProvider from "./context/LoadingContext";
import Home from "./views/Home/Home";
import AppContextProvider from "./context/AppContext";
import SuccessContextProvider from "./context/SuccessContext";
import Schedule from "./views/Schedule/Schedule";
import Modal from "./components/Modal/Modal";
import "bootstrap/dist/css/bootstrap.min.css";
import DateContextProvider from "./context/DateContext";

const App = () => {
  return (
    <Router>
      <AppContextProvider>
        <LoadingContextProvider>
          <SuccessContextProvider>
            <DateContextProvider>
              <Routes>
                <Route path="/home" element={<Home />} />
                <Route path="/schedule" element={<Schedule />} />
              </Routes>
            </DateContextProvider>
          </SuccessContextProvider>
          <Modal />
        </LoadingContextProvider>
      </AppContextProvider>
    </Router>
  );
};

export default App;
