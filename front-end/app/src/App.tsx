import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import LoadingContextProvider from "./context/LoadingContext";
import Home from "./views/Home/Home";
import AppContextProvider from "./context/AppContext";
import SuccessContextProvider from "./context/SuccessContext";

const App = () => {
  return (
    <Router>
      <AppContextProvider>
        <LoadingContextProvider>
          <SuccessContextProvider>
            <Routes>
              <Route path="/home" element={<Home />} />
            </Routes>
          </SuccessContextProvider>
        </LoadingContextProvider>
      </AppContextProvider>
    </Router>
  );
};

export default App;
