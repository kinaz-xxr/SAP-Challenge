// manage the app render view for modal

import { createContext, useContext, useMemo, useState } from "react";

interface IAppContext {
  showModal: boolean;
  setShowModal: React.Dispatch<React.SetStateAction<boolean>>;
  modalContent: any;
  setModalContent: React.Dispatch<React.SetStateAction<any>>;
}

export const AppContext = createContext<IAppContext>({
  showModal: false,
  setShowModal: () => {},
  modalContent: false,
  setModalContent: () => {},
});

const AppContextProvider = (props: { children: any }) => {
  const [showModal, setShowModal] = useState<boolean>(false);
  const [modalContent, setModalContent] = useState<any>(null);

  const returnValue = useMemo(
    () => ({
      showModal,
      setShowModal,
      modalContent,
      setModalContent,
    }),
    [showModal, setShowModal, modalContent, setModalContent]
  );

  return (
    <AppContext.Provider value={returnValue}>{props.children}</AppContext.Provider>
  );
};

export const useAppContext = () => {
    const context = useContext(AppContext);
    if(context === null) {
        throw new Error(`Something went wrong! Cannot get the current app state`);
    }
    return context;
};

export default AppContextProvider;
