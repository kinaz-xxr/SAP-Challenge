import { CircularProgress } from "@mui/material";
import { useLoadingContext } from "../../context/LoadingContext";

// loading component
const Loading = () => {
    const { isLoading, setLoading } = useLoadingContext();

    return isLoading ? (
        <CircularProgress 
            color="secondary"
            size={180}
            thickness={2}
        />
    ) : null;
};

export default Loading;