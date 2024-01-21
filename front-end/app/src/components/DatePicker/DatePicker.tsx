import dayjs from "dayjs";
import { DemoContainer, DemoItem } from "@mui/x-date-pickers/internals/demo";
import { StaticDatePicker } from "@mui/x-date-pickers/StaticDatePicker";
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import Style from './DatePicker.module.scss';
import { useDateContext } from "../../context/DateContext";

export type DatePickerProps = {
  onPickDate: (e: any) => void;
};

const DatePicker = (props: DatePickerProps) => {
  const { currentDate, setDate } = useDateContext();

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <h5 className={Style.Header}>Pick a date to view appointment</h5>
      <DemoItem label="">
        <StaticDatePicker
          defaultValue={dayjs("2022-10-01")}
          onChange={(newDate) => {
            if (!newDate) {
              return;
            }

            const date: string = newDate.format("YYYY-MM-DD");
            console.log(date);
            setDate(date);
            console.log(currentDate);
          }}
          onAccept={props.onPickDate}
        />
      </DemoItem>
    </LocalizationProvider>
  );
};

export default DatePicker;
