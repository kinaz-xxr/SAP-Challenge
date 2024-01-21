import React, { useEffect } from "react";
import LinearChart from "../../components/LinearChart/LinearChart";
import { useDateContext } from "../../context/DateContext";
import ServicesImpl, { Services } from "../../services/services";

// Report Line Chart component
const ReportLineChart = () => {
    // get the data from the backend
    const { currentDate } = useDateContext();
    const services: Services = new ServicesImpl();
    let actualRevenue: number[] = [];
    let lostRevenue: number[] = [];
    
    useEffect(() => {
        services.getRevenue({
            url: "http://127.0.0.1:5000/revenue",
            date: currentDate,
        })
        .then((response) => {
            actualRevenue = response.data['actualRevenue'] as number[];
            lostRevenue = response.data['lostRevenue'] as number[];
            if(actualRevenue.length === 0 || lostRevenue.length === 0) {
                throw new Error(`No revenue data found!!!!`);
            }
            console.log(`Response from revenue: ${response}`);
        })
        .catch((error) => {
            console.error(`Error: ${error}`);
            throw new Error(error);
        })
    }, [currentDate, actualRevenue, lostRevenue, services]);

  return (
    <div>
      <LinearChart 
        xAxis={[{ data: [1.10, 2.10, 3.10, 4.10, 5.10, 6.10, 7.10, 8.10, 9.10, 10.10, 11.10, 12.10, 13.10, 14.10, 15.10, 16.10, 17.10, 18.10, 19.10, 20.10, 21.10, 22.10, 23.10, 24.10, 25.10, 26.10, 27.10, 28.10, 29.10, 30.10, 31.10, 1.11, 2.11, 3.11, 4.11, 5.11, 6.11, 7.11, 8.11, 9.11, 10.11, 11.11, 12.11, 13.11, 14.11, 15.11, 16.11, 17.11, 18.11, 19.11, 20.11, 21.11, 22.11, 23.11, 24.11, 25.11, 26.11, 27.11, 28.11, 29.11, 30.11] }]}
        series={[{ data: actualRevenue }]}
        width={500}
        height={300}
      />
      <LinearChart 
        xAxis={[{ data: [1.10, 2.10, 3.10, 4.10, 5.10, 6.10, 7.10, 8.10, 9.10, 10.10, 11.10, 12.10, 13.10, 14.10, 15.10, 16.10, 17.10, 18.10, 19.10, 20.10, 21.10, 22.10, 23.10, 24.10, 25.10, 26.10, 27.10, 28.10, 29.10, 30.10, 31.10, 1.11, 2.11, 3.11, 4.11, 5.11, 6.11, 7.11, 8.11, 9.11, 10.11, 11.11, 12.11, 13.11, 14.11, 15.11, 16.11, 17.11, 18.11, 19.11, 20.11, 21.11, 22.11, 23.11, 24.11, 25.11, 26.11, 27.11, 28.11, 29.11, 30.11] }]}
        series={[{ data: lostRevenue }]}
        width={500}
        height={300}
      />
      <div style={{display:'flex', justifyContent: 'center'}}>
      <p>
        Revenue: {actualRevenue}
      </p>
      <p>
        Revenue Missed: {actualRevenue}
      </p>
    </div>
    </div>

  );
};

export default ReportLineChart;