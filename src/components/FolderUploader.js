import React, { useState } from 'react';

const FolderUploader = () => {
  const [files, setFiles] = useState([]);

  // 폴더 선택 시 이벤트 핸들러
  const handleFolderSelect = async (e) => {
    const folder = e.target.files[0];

    if (folder) {
      const fileArray = Array.from(folder);

      // 선택된 폴더의 파일 목록을 출력
      setFiles(fileArray.map((file) => ({ path: URL.createObjectURL(file) })));
    }
  };

  return (
    <div>
      {/* 폴더 선택을 위한 input */}
      <input
        type="file"
        webkitdirectory="true"
        directory="true"
        onChange={handleFolderSelect}
      />

      {/* 선택된 파일 목록 출력 */}
      <ul>
        {files.map((file, index) => (
          <li key={index}>{file.path}</li>
        ))}
      </ul>
    </div>
  );
};

export default FolderUploader;

// import React, { useCallback, useState } from 'react';
// import { useDropzone } from 'react-dropzone';

// const FolderUploader = () => {
//   const [files, setFiles] = useState([]);

//   const onDrop = useCallback((acceptedFiles) => {
//     setFiles(acceptedFiles);
//   }, []);

//   const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

//   return (
//     <div>
//       {/* 드롭존에 스타일과 이벤트 핸들러 적용 */}
//       <div {...getRootProps()} style={dropzoneStyle}>
//         <input {...getInputProps()} />
//         {isDragActive ? (
//           <p>폴더를 놓아주세요!</p>
//         ) : (
//           <p>폴더를 드래그하거나 클릭하여 선택하세요.</p>
//         )}
//       </div>

//       {/* 선택된 파일 목록 출력 */}
//       <ul>
//         {files.map((file) => (
//           <li key={file.path}>{file.path}</li>
//         ))}
//       </ul>
//     </div>
//   );
// };

// // 드롭존 스타일
// const dropzoneStyle = {
//   border: '2px dashed #cccccc',
//   borderRadius: '4px',
//   padding: '20px',
//   textAlign: 'center',
//   cursor: 'pointer',
// };

// export default FolderUploader;
