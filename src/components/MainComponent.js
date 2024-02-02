// MainComponent.js
import React, { useState } from 'react';
import styled from 'styled-components';  // 이 부분을 추가하세요
import FileUpload from './FileUpload';
import ImageViewer from './ImageViewer';

const Container = styled.div`
  display: flex;
  height: 100%;
  flex-direction: column;
`;

const ImageUpload = styled.div`
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
`;

const Button = styled.div`
  display: flex;
  justify-content: center;
`;

const Label = styled.label`
  cursor: pointer;
  font-size: 1em;
`;

const ChooseFileInput = styled.input`
  visibility: hidden;
`;

const FileContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
`;

const FileInput = styled.div`
  display: flex;
  align-items: center;
  border-bottom: solid 2px black;
  width: 60%;
  height: 30px;
`;

const FileName = styled.p`
  margin-left: 5px;
`;

const ButtonContainer = styled.div`
  width: 15%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 10px;
  background-color: black;
  color: white;
  border-radius: 30px;
  padding: 10px;
  font-size: 0.8em;
  cursor: pointer;
`;

const ImageShow = styled.div`
  z-index: -1;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  width: 100%;
  height: 100%;
`;

const Img = styled.img`
  position: absolute;
`;

const MainComponent = () => {
  const [uploadedImage, setUploadedImage] = useState(null);

  const handleImageSubmit = ({ fileName, image }) => {
    // 서버로 이미지 업로드 요청을 보낼 수도 있습니다.
    // 혹은 다른 처리를 수행할 수 있습니다.
    setUploadedImage(image);
  };

  return (
    <Container>
      <FileUpload onImageSubmit={handleImageSubmit} />
      <ImageViewer image={uploadedImage} />
    </Container>
  );
};

export default MainComponent;
