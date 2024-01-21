import { error } from "console";
import http from "../http-common";
import { sendDataProps } from "../types/data";
import { Data } from "../types/data";
import { PostDateReq } from "../types/date";
import GetRevenueRequest from "../types/revenue";

// rest services
export interface Services {
  sendData(req: sendDataProps): Promise<any>;
  fileUpload(uploadFile: File, onUploadProgress: any): Promise<any>;
  getFiles(): Promise<any>;
  postDate(req: PostDateReq): Promise<any>;
  getRevenue(req: GetRevenueRequest): Promise<any>;
};

class ServicesImpl implements Services {
  async sendData(req: sendDataProps) {
    return http
      .post<Data>(req.url, req.data)
      .then((response) => {
        if (response && response.data) {
          return response.data;
        } else {
          throw new Error("Invalid response format: 'data' property not found");
        }
      })
      .catch((error) => {
        console.error(error);
        throw error;
      });
  }

  fileUpload(uploadFile: File, onUploadProgress: any): Promise<any> {
    let formData = new FormData();

    formData.append("file", uploadFile);

    return http.post("http://127.0.0.1:5000/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
      onUploadProgress,
    });
  }

  getFiles(): Promise<any> {
    return http.get("http://127.0.0.1:5000/files");
  }

  postDate(req: PostDateReq): Promise<any> {
    return http.post<PostDateReq>(req.url, req.date, {
      headers: {
        "Content-Type": "application/json",
      },
    });
  };

  getRevenue(req: GetRevenueRequest): Promise<any> {
    return http.get<GetRevenueRequest>(req.url, {
      data: req.date
    });
  };
}

export default ServicesImpl;
