// data types
export type Data = {
    bookingDateTime: string,
    appointmentDateTime: string,
    carType: string,
};

export type sendDataProps = {
    url: string,
    data: Array<Data>
};
