// button component
import styles from "./Button.module.scss";

export type ButtonProps = {
  label?: string;
  onClick: (event: any) => void;
  className?: string;
};

const Button = (props: ButtonProps) => {
  return (
    <button className={props.className ? props.className : styles.Button}>
      {props.label}
    </button>
  );
};

export default Button;
