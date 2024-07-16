import React, { Component } from "react";
import styled from "styled-components";
import oc from "open-color";
import "../App.css";

// import Header from "../components/Header.js";
import Folder from "../assets/Folder.png";
import FolderUploader from "./FolderUploader.js";

class ImgUpload extends Component {
  render() {
    return (
      <UploadContainer>
        {/* <Header /> */}
        
        <Title>이 폴더는 이미지가 없는 폴더 입니다 ❗</Title>
        <SubTitle>
          이미지들을 한 폴더에 넣은 후 <br />
          이미지들이 저장된 폴더를 업로드 해주세요
        </SubTitle>
        <Upload>
          <ShareUpload>
            <img
              src={Folder}
              alt="logo img"
              style={{ width: "15em", margin: "30px auto" }}
            />
            <CenteredFolderUploader>
              <FolderUploader />
            </CenteredFolderUploader>
          </ShareUpload>
        </Upload>
      </UploadContainer>
    );
  }
}

export default ImgUpload;

const UploadContainer = styled.div`
    display: flex;
    flex-direction: column;
    justify-contents : center;
    max-width: 100%
    height:100vh;
    background-color: ${oc.grape[0]}
    
`;

const Title = styled.div`
  text-align: center;
  align-items: center;
  margin: 0 auto;
  padding-top: 45px;
  font-weight: bold;
  font-size: 25px;
  font-family: 'yg-jalnan';
`;

const SubTitle = styled.div`
  margin: 0 auto;
  text-align: center;
`;

const Upload = styled.div`
  display: flex;
  flex-direction: row;
  margin: 10px auto;
  text-align: center;
  align-items: center;
  max-width: 100%;
  height: 500px;
  margin-bottom: 800px;
  border: 1px solid #cccccc;
`;

const ShareUpload = styled.div`
  width: 400px;
  height: 500px;
  background-color: #deabde;
  padding-top: 50px;
`;

// FolderUploader를 가운데 정렬하기 위한 스타일
const CenteredFolderUploader = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  margin: 20px auto;
  margin-left: 120px;
`;
