// FileUpload.js
import React, { useState } from 'react';

const FileUpload = ({ onImageSubmit }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleSubmit = () => {
    if (selectedFile) {
      const fileName = selectedFile.name;
      const imageDataUrl = URL.createObjectURL(selectedFile);
      onImageSubmit({ fileName, image: imageDataUrl });
    }
  };

  return (
    <div className="image-upload">
      <form>
        <div className="button">
          <label htmlFor="chooseFile">👉 CLICK HERE! 👈</label>
        </div>
        <input
          type="file"
          id="chooseFile"
          name="chooseFile"
          accept="image/*"
          onChange={handleFileChange}
        />
      </form>
      <div className="fileContainer">
        <div className="fileInput">
          <p>FILE NAME: </p>
          <p>{selectedFile ? selectedFile.name : 'No file selected'}</p>
        </div>
        <div className="buttonContainer">
          <div className="submitButton" onClick={handleSubmit}>
            SUBMIT
          </div>
        </div>
      </div>
    </div>
  );
};

export default FileUpload;
