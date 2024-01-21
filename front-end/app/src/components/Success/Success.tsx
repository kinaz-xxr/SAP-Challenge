import { useSuccessContext } from "../../context/SuccessContext";
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';

// success component will be rendered -> when the file is uploaded successfully
const Success = () => {
    const { isSuccess } = useSuccessContext();

    return isSuccess ? (
        // render the success component in the modal
        <Alert severity="success">
            <AlertTitle>Success</AlertTitle>
            Successfully 
        </Alert>
    ) : null;
};

export default Success;