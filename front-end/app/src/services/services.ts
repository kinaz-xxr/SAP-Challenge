import http from "../http-common";
import { sendDataProps } from "../types/data";
import { Data } from "../types/data";

// rest services
export interface Services {
    fileUpload(uploadFile: File, onUploadProgress: any): Promise<any>;
    getFiles(): Promise<any>;
};

class ServicesImpl implements Services {
    async fileUpload(uploadFile: File, onUploadProgress: any): Promise<any> {
        let formData = new FormData();

        formData.append("file", uploadFile);

        return http.post("/upload", formData, {
            headers: {
                "Content-Type" : "multipart/form-data",
            },
            onUploadProgress,
        })
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
    
    async getFiles(): Promise<any> {
        return http.get("/files")
        .then((response) => {
            console.log(response);
        })
        .catch((error) => {
            console.error(error);
        })
    };
};  

export default ServicesImpl;