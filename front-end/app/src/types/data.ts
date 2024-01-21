// data types
type Data = {
    bookDateTime: Date,
    appointDateTime: Date,
    carType: string,
};

type sendDataProps = {
    url: string,
    data: Data,
};

export default sendDataProps;