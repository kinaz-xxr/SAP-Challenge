import { useCallback, useEffect, useState } from "react";
import { useLoadingContext } from "../../context/LoadingContext";
import CircularProgress from "@mui/material/CircularProgress";
import IFile from "../../types/file";
import Services from "../../services/services";
import ServicesImpl from "../../services/services";
import styles from "./UploadFile.module.scss";
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
  const upload = useCallback(async () => {
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
  }, [currentFile, setCurrentFile, setProgress, setMessage]);

  // when the file is uploaded -> get the files to update the file info
  useEffect(() => {
    getFiles()
      .then((response) => {
        setFileInfos(response.data);
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
          <div className={styles['text-above-button']}>
            <label htmlFor="csv_file">Import your .csv file for optimization:</label>
          </div>
            <input id="csv_file" type="file" name="csv_file" accept="image/png, image/jpeg" />
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
