// FolderList.js

import React from "react";
import Folder from "./Folder";

const FolderList = ({ folders, onFolderClick }) => {
  return (
    <div style={{ textAlign: "center", alignItems: "center" }}>
      {folders.map((folder, index) => (
        <Folder key={index} folderName={folder.name} onClick={() => onFolderClick(folder)} />
      ))}
    </div>
  );
};

export default FolderList;
