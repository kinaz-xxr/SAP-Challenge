import { CircularProgress } from "@mui/material";
import { useLoadingContext } from "../../context/LoadingContext";
import { styled } from '@mui/system';   

const CenteredContainer = styled('div')({
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  position: 'fixed',
  width: '100%',
  top: '38%',
});

// loading component
const Loading = () => {
    const { isLoading, setLoading } = useLoadingContext();

    return isLoading ? (
        <CenteredContainer>
            <CircularProgress 
            color="primary"
            size={120}
            thickness={2}  
        />
        </CenteredContainer>
    ) : null;
};

export default Loading;