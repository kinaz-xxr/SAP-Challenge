import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import LoadingContextProvider from "./context/LoadingContext";
import Home from "./views/Home/Home";

const App = () => {
  return (
    <Router>
      <LoadingContextProvider>
        <Routes>
          <Route path="/home" element={<Home />} />
        </Routes>
      </LoadingContextProvider>
    </Router>
  );
};

export default App;
