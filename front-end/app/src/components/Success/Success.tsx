import { useSuccessContext } from "../../context/SuccessContext";
import styles from './Success.module.scss';

// success component will be rendered -> when the file is uploaded successfully
const Success = () => {
    const { isSuccess } = useSuccessContext();

    return isSuccess ? (
        // render the success component in the modal
        <div className="">

        </div>
    ) : null;
};

export default Success;