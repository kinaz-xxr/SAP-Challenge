// linear chart component
import * as React from 'react';
import { LineChart } from '@mui/x-charts/LineChart';
import ServicesImpl, { Services } from '../../services/services';

export type LinearChartProps = {
    xAxis: {
        data: number[],
    }[],
    series: {
        data: number[],
    }[],
    width: number,
    height: number,
};

const LinearChart = (
    props: LinearChartProps
) => {

    return (
        <LineChart 
            xAxis={props.xAxis}
            series={props.series}
            width={props.width}
            height={props.height}
        />
    );
};

export default LinearChart;