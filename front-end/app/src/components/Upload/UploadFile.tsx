import { useCallback, useEffect, useState } from "react";
import { useLoadingContext } from "../../context/LoadingContext";
import CircularProgress from "@mui/material/CircularProgress";
import IFile from "../../types/file";
import Services from "../../services/services";
import ServicesImpl from "../../services/services";
import styles from "./UploadFile.module.scss";
import csv2json from "../../utils/CSV2Json";
import { Data } from "../../types/data";

// component to upload the csv file
const UploadFile = () => {
  const [currentFile, setCurrentFile] = useState<File>();
  const [progress, setProgress] = useState<number>(0);
  const [message, setMessage] = useState<string>("");
  const [fileInfos, setFileInfos] = useState<Array<IFile>>();
  const { isLoading, setIsLoading, setLoading } = useLoadingContext();

  const services: Services = new ServicesImpl();

  const { fileUpload, getFiles } = services;

  const handleUploadFile = (e: React.ChangeEvent<any>) => {
    // when the user click -> upload file
    const { files } = e.target;
    const selectedFiles = files as FileList;
    setCurrentFile(selectedFiles?.[0]);
    setProgress(0);
  };

  // upload file function
  const upload = async () => {
    setProgress(0);
    if (!currentFile) return;

    fileUpload(currentFile, (event: any) => {
      setProgress(Math.round((100 * event.loaded) / event.total));
    })
      .then((files) => {
        setFileInfos(files);
      })
      .catch((error) => {
        setProgress(0);

        if (
          error.response &&
          error.response.data &&
          error.response.data.message
        ) {
          setMessage(error.response.data.message);
        } else {
          setMessage("Could not upload the file!");
        }

        setCurrentFile(undefined);
      });
  };

  // after the file is uploaded -> parse the file and send the data to the backend
  const onParsingCSV = useCallback(
    async (props: { csvFilePath: string }) => {
      const helperProp = {
        csvFilePath: props.csvFilePath,
      };
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve(csv2json(helperProp));
        }, 2000);
      });
    },
    [csv2json]
  );

  const onSendingData = useCallback(
    async (props: { csvFilePath: string; url: string }) => {
      try {
        setLoading(true);

        const jsonArray = (await onParsingCSV({
          csvFilePath: props.csvFilePath,
        })) as Array<Data>;

        // send the data to the backend
        services
          .sendData({
            url: props.url,
            data: jsonArray,
          })
          .then((response) => {
            console.log(JSON.stringify(response));
          })
          .catch((error) => {
            console.error(`Error: ${error}`);
          });
      } catch (error) {
        console.error(`Error fetching data: `, error);
      } finally {
        setLoading(false);
      }
    },
    [onParsingCSV, setLoading]
  );

  // when the file is uploaded -> get the files to update the file info
  useEffect(() => {
    getFiles()
      .then((response) => {
        setFileInfos(response.data);
        onSendingData(
          {
            csvFilePath: "http://localhost:3000/files",
            url: "http://127.0.0.1:5000/predict",
          }
        );
      })
      .catch((error) => {
        setMessage(error.response.data.message);
        console.error(`Error while getting the file: ${error}`);
      });
  }, []); // unmount the component

  return (
    <div>
      <div className={styles.UploadFile}>
        <div className={styles.UploadFile__chooseFileButton}>
          <label className="btn btn-default p-0">
            <input type="file" onChange={handleUploadFile} />
          </label>
        </div>

        <div className="col-4">
          <button
            className="btn btn-success btn-sm"
            disabled={!currentFile}
            onClick={upload}
          >
            Upload
          </button>
        </div>
      </div>

      {currentFile && (
        <div className="progress my-3">
          <div
            className="progress-bar progress-bar-info"
            role="progressbar"
            aria-valuenow={progress}
            aria-valuemin={0}
            aria-valuemax={100}
            style={{ width: progress + "%" }}
          >
            {progress}%
          </div>
        </div>
      )}

      {message && (
        <div className="alert alert-secondary mt-3" role="alert">
          {message}
        </div>
      )}

      <div className="card mt-3">
        <div className="card-header">List of Files</div>
        <ul className="list-group list-group-flush">
          {fileInfos &&
            fileInfos.map((file, index) => (
              <li className="list-group-item" key={index}>
                <a href={file.url}>{file.name}</a>
              </li>
            ))}
        </ul>
      </div>
    </div>
  );
};

export default UploadFile;
