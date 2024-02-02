import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFolder } from "@fortawesome/free-solid-svg-icons";
import Button from 'react-bootstrap/Button';

const Folder = ({ folderName, onClick }) => {
  return (
    <Button
      variant="outline-success"
      style={{
        margin: "10px",
        maxWidth: "15rem",
        border: "solid 1px #cccccc",
        backgroundColor: "white",
        color: "black"
      }}
      onClick={onClick}
    >
      <FontAwesomeIcon icon={faFolder} style={{ height: "20vh", color: "#A286DB" }} />
      <div>{folderName}</div>
    </Button>
  );
};

export default Folder;