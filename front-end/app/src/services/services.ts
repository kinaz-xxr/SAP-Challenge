import http from "../http-common";
import { sendDataProps } from "../types/data";
import { Data } from "../types/data";

// rest services
export interface Services {
    sendData(req: sendDataProps): Promise<any>;
    fileUpload(uploadFile: File, onUploadProgress: any): Promise<any>;
    getFiles(): Promise<any>;
};

class ServicesImpl implements Services {
    async sendData(req: sendDataProps) {
        return http.post<Data>(
            req.url,
            req.data,
        )
        .then((response) => {
            if(response && response.data) {
                return response.data;
            } else {
                throw new Error("Invalid response format: 'data' property not found")
            }
        })
        .catch((error) => {
            console.error(error);
            throw error;
        });
    };

    fileUpload(uploadFile: File, onUploadProgress: any): Promise<any> {
        let formData = new FormData();

        formData.append("file", uploadFile);

        return http.post("/upload", formData,{
            headers: {
                "Content-Type" : "multipart/form-data",
            },
            onUploadProgress,
        });
    };
    
    getFiles(): Promise<any> {
        return http.get("/files");
    };
};  

export default ServicesImpl;