import React, { createContext, useContext, useMemo, useState } from "react";

// keep track of the label of the button
export interface IButtonContext {
    label: string;
    setLabel: React.Dispatch<React.SetStateAction<string>>;
    onClick: (event: any) => void;
    setOnClick: React.Dispatch<React.SetStateAction<any>>;
};

export const ButtonContext = createContext<IButtonContext>({
    label: "",
    setLabel: () => {},
    onClick: () => {},
    setOnClick: () => {},
});

const ButtonContextProvider = (props: {
    children: any
}) => {
    const [label, setLabel] = useState<string>("");
    const [onClick, setOnClick] = useState<any>(undefined);

    const returnValue = useMemo(
        () => ({
            label,
            setLabel,
            onClick,
            setOnClick
        }), [label, setLabel, onClick, setOnClick]
    );

    return (
        <ButtonContext.Provider value={returnValue}>{props.children}</ButtonContext.Provider>
    );
};

export const useButtonContext = () => {
    const context = useContext(ButtonContext);
    if(context === null) {
        throw new Error(`Something went wrong!`);
    };
    return context;
};

export default ButtonContextProvider;