import { IconButton } from "@mui/material";
import { useAppContext } from "../../context/AppContext";
import CloseIcon from "@mui/icons-material/Close";
import styles from "./Modal.module.scss";

const Modal = () => {
  const { showModal, setShowModal, modalContent, setModalContent } =
    useAppContext();

  // function to close the modal when onClick
  const handleCloseModal = () => {
    setShowModal(false);
    setModalContent(undefined);
  };

  return showModal ? (
    <div
      className={styles.Modal}
      onClick={() => {
        handleCloseModal();
      }}
    >
      <div
        className={styles.Modal__container}
        onClick={(e) => {
          e.stopPropagation();
        }}
      >
        <IconButton
          className={styles.Modal__container__closeButton}
          onClick={() => {
            handleCloseModal();
          }}
        >
          <CloseIcon />
        </IconButton>
        <div className={styles.Modal__container__content}>{modalContent}</div>
      </div>
    </div>
  ) : null;
};
