import { error } from "console";
import { createContext, useContext, useMemo, useState } from "react";

// success context hook
interface ISuccessContext {
  isSuccess: boolean;
  setIsSuccess: React.Dispatch<React.SetStateAction<boolean>>;
  setSuccess: (value: boolean) => void;
}

export const SuccessContext = createContext<ISuccessContext>({
  isSuccess: false,
  setIsSuccess: () => {},
  setSuccess: () => {},
});

const SuccessContextProvider = (props: { children: any }) => {
  const [isSuccess, setIsSuccess] = useState<boolean>(false);

  const setSuccess = (value: boolean) => {
    try {
      setIsSuccess(value);
    } catch (error) {
      console.error(`Error while setting success state: ${error}`);
    }
  };

  const returnValue = useMemo(
    () => ({ isSuccess, setIsSuccess, setSuccess }),
    [isSuccess, setIsSuccess, setSuccess]
  );

  return (
    <SuccessContext.Provider value={returnValue}>
        {props.children}
    </SuccessContext.Provider>
  );
};

export const useSuccessContext = () => {
    const context = useContext(SuccessContext);
    if(context === null) {
        throw new Error(`Error while getting the current success state: ${error}`);
    }
    return context;
};

export default SuccessContextProvider;
