import React, { useState } from 'react';
import FileUpload from './FileUpload';
import ImageViewer from './ImageViewer';

const MainComponent = () => {
  const [uploadedImage, setUploadedImage] = useState(null);

  const handleImageSubmit = ({ fileName, image }) => {
    // 서버로 이미지 업로드 요청을 보낼 수도 있습니다.
    // 혹은 다른 처리를 수행할 수 있습니다.
    setUploadedImage(image);
  };

  return (
    <div className="container">
      <FileUpload onImageSubmit={handleImageSubmit} />
      <ImageViewer image={uploadedImage} />
    </div>
  );
};

export default MainComponent;