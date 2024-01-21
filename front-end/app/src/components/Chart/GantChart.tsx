import React, { useState } from "react";
// Import Highcharts
import Highcharts from "highcharts/highcharts-gantt";
import HighchartsReact from "highcharts-react-official";
import { blue, green, lightBlue, orange, red, yellow } from "@mui/material/colors";

const GantChart = (taskData : any) => {

  console.log(taskData)

  let table1 = taskData['table1']

  let tableColorMapper : any = {
    'compact' : lightBlue, 
    'medium' : blue, 
    'full-size' : red, 
    'class 1 truck' : yellow, 
    'class 2 truck' : orange, 
  }

  let firstTable = []
  let secondTable = []
  let thirdTable = []
  let fourthTable = []
  let fifthTable = []
  let sixthTable = []
  let seventhTable = []
  let eightTable = []
  let nineTable = []
  let tenTable = []
  for(let i = 0; i < taskData['table1']!.dateStartAppointment; i++) {
    firstTable.push({
      y: 0, 
      start: taskData['table1']!.dateStartAppointment[i], 
      end: taskData['table1']!.dateEndAppointment[i], 
      color: tableColorMapper[taskData['table1']!.carType[i]]
    })

    secondTable.push({
      y: 1, 
      start: taskData['table2']!.dateStartAppointment[i], 
      end: taskData['table2']!.dateEndAppointment[i], 
      color: tableColorMapper[taskData['table2']!.carType[i]]
    })

    thirdTable.push({
      y: 2, 
      start: taskData['table3']!.dateStartAppointment[i], 
      end: taskData['table3']!.dateEndAppointment[i], 
      color: tableColorMapper[taskData['table3']!.carType[i]]
    })

    fourthTable.push({
      y: 3, 
      start: taskData['table4']!.dateStartAppointment[i], 
      end: taskData['table4']!.dateEndAppointment[i], 
      color: tableColorMapper[taskData['table4']!.carType[i]]
    })

    fifthTable.push({
      y: 4, 
      start: taskData['table5']!.dateStartAppointment[i], 
      end: taskData['table5']!.dateEndAppointment[i], 
      color: tableColorMapper[taskData['table5']!.carType[i]]
    })

    sixthTable.push({
      y: 5, 
      start: taskData['table6']!.dateStartAppointment[i], 
      end: taskData['table6']!.dateEndAppointment[i], 
      color: tableColorMapper[taskData['table6']!.carType[i]]
    })

    seventhTable.push({
      y: 6, 
      start: taskData['table7']!.dateStartAppointment[i], 
      end: taskData['table7']!.dateEndAppointment[i], 
      color: tableColorMapper[taskData['table7']!.carType[i]]
    })

    eightTable.push({
      y: 7, 
      start: taskData['table8']!.dateStartAppointment[i], 
      end: taskData['table8']!.dateEndAppointment[i], 
      color: tableColorMapper[taskData['table8']!.carType[i]]
    })

    nineTable.push({
      y: 8, 
      start: taskData['table9']!.dateStartAppointment[i], 
      end: taskData['table9']!.dateEndAppointment[i], 
      color: tableColorMapper[taskData['table9']!.carType[i]]
    })

    tenTable.push({
      y: 9, 
      start: taskData['table10']!.dateStartAppointment[i], 
      end: taskData['table10']!.dateEndAppointment[i], 
      color: tableColorMapper[taskData['table10']!.carType[i]]
    })
  }

  
  


  const [options] = useState({
    series: [
      {
        data: [...firstTable, ...secondTable, ...thirdTable, ...fourthTable, ...fifthTable, ...sixthTable,
               ...seventhTable, ...eightTable, nineTable]
      }
    ]
  });

  return (
    <HighchartsReact
      highcharts={Highcharts}
      constructorType={"ganttChart"}
      options={options}
    />
  );
};

export default GantChart