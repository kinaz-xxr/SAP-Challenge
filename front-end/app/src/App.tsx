import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import LoadingContextProvider from "./context/LoadingContext";
import Home from "./views/Home/Home";
import AppContextProvider from "./context/AppContext";

const App = () => {
  return (
    <Router>
      <AppContextProvider>
        <LoadingContextProvider>
          <Routes>
            <Route path="/home" element={<Home />} />
          </Routes>
        </LoadingContextProvider>
      </AppContextProvider>
    </Router>
  );
};

export default App;
