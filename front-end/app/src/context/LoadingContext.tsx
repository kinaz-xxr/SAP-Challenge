// loading context

import { createContext, useContext, useMemo, useState } from "react";

interface ILoadingContext {
    isLoading: boolean;
    setIsLoading: React.Dispatch<React.SetStateAction<boolean>>;
    setLoading: (value: boolean) => void;
};

export const LoadingContext = createContext<ILoadingContext>({
    isLoading: false,
    setIsLoading: () => {},
    setLoading: () => {},
});

const LoadingContextProvider = (
    props: {
        children: any
    }
) => {
    const [isLoading, setIsLoading] = useState<boolean>(false); // default false

    // set loading state
    const setLoading = (value: boolean) => {
        try {
            setIsLoading(value);
            console.log(`New loading: ${isLoading}`)
        } catch(error) {
            console.error(`Error changing loading state for the app: ${error}`);
        };
    };

    const returnValue = useMemo(() => ({
        isLoading,
        setIsLoading,
        setLoading
    }), [isLoading, setIsLoading, setLoading]);

    return (
        <LoadingContext.Provider value={returnValue}>
            {props.children}
        </LoadingContext.Provider>
    );
};

export const useLoadingContext = () => {
    const context = useContext(LoadingContext);
    if(context === null) {
        throw new Error(`Something went wrong! Cannot receive the current context!`);
    };
    return context;
};

export default LoadingContextProvider;