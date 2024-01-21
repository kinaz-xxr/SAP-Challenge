import fs from "fs";
import csv from "csv-parser";
import { Data } from "../types/data";

// helper function to parse csv to json
const csv2json = async (props: {
  csvFilePath: string;
}): Promise<Array<Data>> => {
  // parse the csv to json
  const jsonArray: Array<{
    bookingDateTime: string;
    appointmentDateTime: string;
    carType: string;
  }> = [];

  fs.createReadStream(props.csvFilePath)
    .pipe(csv())
    .on("data", (row: Data) => {
      const {
        bookingDateTime: bookingDateTime,
        appointmentDateTime: appointmentDateTime,
        carType: carType,
      } = row;

      jsonArray.push({
        bookingDateTime,
        appointmentDateTime,
        carType,
      });
    })
    .on("end", () => {
      console.log(JSON.stringify(jsonArray, null, 2)); // print the json array after being parse
    });

  return jsonArray;
};

export default csv2json;