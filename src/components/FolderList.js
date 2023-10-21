import React from "react";
import Folder from "./Folder";

const FolderList = ({ folders }) => {
  return (
    <div style={{ textAlign: "center", alignItems: "center" }}>
      {folders.map((folder, index) => (
        <Folder key={index} folderName={folder.name} />
      ))}
    </div>
  );
};

export default FolderList;
