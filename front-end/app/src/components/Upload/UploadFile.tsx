import React, { ChangeEvent, useState, useEffect, useCallback } from 'react';
import { useLoadingContext } from "../../context/LoadingContext";
import CircularProgress from "@mui/material/CircularProgress";
import IFile from "../../types/file";
import Services from "../../services/services";
import ServicesImpl from "../../services/services";
import styles from "./UploadFile.module.scss";
import { useSuccessContext } from "../../context/SuccessContext";
import { useAppContext } from "../../context/AppContext";
import Success from "../Success/Success";

// component to upload the csv file
const UploadFile = () => {
  const [currentFile, setCurrentFile] = useState<File>();
  const [progress, setProgress] = useState<number>(0);
  const [message, setMessage] = useState<string>("");
  const [fileInfo, setFileInfo] = useState<IFile | undefined>(undefined); // Changed from IFile to IFile[] | undefined
  const { isLoading, setIsLoading, setLoading } = useLoadingContext();
  const { setSuccess } = useSuccessContext();
  const { setShowModal } = useAppContext();

  const services: Services = new ServicesImpl();

  const { fileUpload, getFiles } = services;

  const selectFile = (event: ChangeEvent<HTMLInputElement>) => {
    const { files } = event.target;
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
      .then((file) => {
        setFileInfo(file);
        // success upload -> success component render
        setSuccess(true);
        setTimeout(() => {
          setSuccess(false);
          setShowModal(false);
        }, 2000); // show success component for 2 seconds

        // the step 1 button becomes the success
        
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
  }, [currentFile, setCurrentFile, setProgress, setMessage, fileUpload, setSuccess, setShowModal]);

  // when the file is uploaded -> get the files to update the file info
  useEffect(() => {
    getFiles()
      .then((response) => {
        setFileInfo(response.data);
      })
      .catch((error) => {
        setMessage(error.response.data.message);
        console.error(`Error while getting the file: ${error}`);
      });
  }, []); // unmount the component

  return (
    <div>
      <div className="row">
        <div className="col-8">
          <label className="btn btn-default p-0">
            <input type="file" onChange={selectFile} />
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

      <Success />
      <div className="card mt-3">
        <div className="card-header">List of Files</div>
        <ul className="list-group list-group-flush">
          {fileInfo && 
            <a href={fileInfo.url}>{fileInfo.name}</a>
          }
        </ul>
      </div>
    </div>
  );
};

export default UploadFile;
