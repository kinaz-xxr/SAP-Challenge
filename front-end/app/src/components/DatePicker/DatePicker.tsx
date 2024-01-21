import dayjs from "dayjs";
import { DemoContainer, DemoItem } from "@mui/x-date-pickers/internals/demo";
import { StaticDatePicker } from "@mui/x-date-pickers/StaticDatePicker";
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import Style from './DatePicker.module.scss';

export type DatePickerData = {
  date: string;
};

export const defaultDatePickerData: DatePickerData = {
  date: "2022-10-01",
};

export type setDate = (newDate: DatePickerData) => void;

export type DatePickerProps = {
  currentDate: DatePickerData;
  setCurrentDate: setDate;
  onPickDate: (e: any) => void;
};

const DatePicker = (props: DatePickerProps) => {
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
            props.setCurrentDate({ ...props.currentDate, date });
            console.log(props.currentDate);
          }}
          onAccept={props.onPickDate}
        />
      </DemoItem>
    </LocalizationProvider>
  );
};

export default DatePicker;
