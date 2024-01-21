import React, { createContext, useContext, useMemo, useState } from "react";

interface IDateContext {
    currentDate: string;
    setCurrentDate: React.Dispatch<React.SetStateAction<string>>;
    setDate: (newValue: string) => void;
};

export const DateContext = createContext<IDateContext>({
    currentDate: "2022-10-01",
    setCurrentDate: () => {},
    setDate: () => {},
});

const DateContextProvider = (
    props: { children: any }
) => {
    const [currentDate, setCurrentDate] = useState<string>("2022-10-01");
    const setDate = (newValue: string) => {
        try {
            setCurrentDate(newValue);
        } catch(error) {
            console.error(`Error: ${error}`);
        }
    };

    const returnValue = useMemo(() => ({
        currentDate,
        setCurrentDate,
        setDate,
    }), [currentDate, setCurrentDate, setDate]);

    return (
        <DateContext.Provider value={returnValue}>
            {props.children}
        </DateContext.Provider>
    );
};

export const useDateContext = () => {
    const context = useContext(DateContext);
    if(!context) {
        throw new Error(`Error with date context!`);
    };
    return context;
};

export default DateContextProvider;