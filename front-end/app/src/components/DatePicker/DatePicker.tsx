import dayjs from "dayjs";
import { DemoContainer, DemoItem } from "@mui/x-date-pickers/internals/demo";
import { StaticDatePicker } from "@mui/x-date-pickers/StaticDatePicker";
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';

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
  onPickDate: (e: React.KeyboardEvent<HTMLInputElement>) => void;
};

const DatePicker = (props: DatePickerProps) => {
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <DemoItem label="Static variant">
        <StaticDatePicker
          defaultValue={dayjs("2022-10-01")}
          onChange={(newDate) => {
            if (!newDate) {
              return;
            }

            const date: string = newDate.format("YYYY-MM-DD");
            props.setCurrentDate({ ...props.currentDate, date });
          }}
        />
      </DemoItem>
    </LocalizationProvider>
  );
};

export default DatePicker;
