// Categorize.js

import React, { useState } from "react";
import styled from "styled-components";
import oc from "open-color";
import "../App.css";
import Container from "react-bootstrap/Container";

import FolderList from "../components/FolderList";
import Header from "../components/Header2.js";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Button from "react-bootstrap/Button";
import { faChevronRight } from "@fortawesome/free-solid-svg-icons";
import Imgshow2 from "../components/Imgshow2";
import FolderUploader from "../components/FolderImgUpload.js";
import { useNavigate } from "react-router-dom";
import Photo from "../assets/love.png";
import PhotoEdit from "../pages/Edit.js";

// 이미지 데이터를 가져오는 함수
const getImagesByFolderName = (folderName) => {
  // 각 폴더에 대한 이미지 데이터를 가져오는 로직을 작성하세요.
  // 예를 들어, "공유폴더 1" 폴더에 대한 이미지 데이터를 가져오려면:
  if (folderName === "요코하마") {
    return [
      { src: Photo, title: "요코하마" },{ src: Photo, title: "요코하마" },{ src: Photo, title: "요코하마" },{ src: Photo, title: "요코하마" },
      
      // 다른 이미지 정보를 추가할 수 있습니다.
    ];
  } else if (folderName === "20231117") {
    return [
      { src: Photo, title: "2023-11-17" },{ src: Photo, title: "2023-11-17" },{ src: Photo, title: "2023-11-17" },{ src: Photo, title: "2023-11-17" }
      // 서혜인 폴더에 대한 이미지 데이터
    ];
 
  } else {
    // 기본적으로 빈 배열 반환
    return [];
  }
};

const folders = [
  {
    name: "일본여행",
    subfolders: [
      {
        name: "서혜인",
        subfolders: [
          { 
            name: "장소별", 
            subfolders: [
              { name: "요코하마", subfolders: [], images: getImagesByFolderName("장소별", "장소1") },
              { name: "아키하바라", subfolders: [], images: getImagesByFolderName("장소별", "장소2") },
              { name: "사쿠라기초", subfolders: [], images: getImagesByFolderName("장소별", "장소3") }
            ] 
          },
          { 
            name: "시간별", 
            subfolders: [
              { name: "20231117", subfolders: [], images: getImagesByFolderName("시간별", "시간1") },
              { name: "20231118", subfolders: [], images: getImagesByFolderName("시간별", "시간2") },
              { name: "20231119", subfolders: [], images: getImagesByFolderName("시간별", "시간3") }
            ] 
          }
        ],
      },
      {
        name: "용수진",  
        subfolders: [
          { 
            name: "장소별", 
            subfolders: [
              { name: "요코하마", subfolders: [], images: getImagesByFolderName("장소별", "장소1") },
              { name: "아키하바라", subfolders: [], images: getImagesByFolderName("장소별", "장소2") },
              { name: "사쿠라기초", subfolders: [], images: getImagesByFolderName("장소별", "장소3") }
            ] 
          },
          { 
            name: "시간별", 
            subfolders: [
              { name: "20231117", subfolders: [], images: getImagesByFolderName("시간별", "시간1") },
              { name: "20231118", subfolders: [], images: getImagesByFolderName("시간별", "시간2") },
              { name: "20231119", subfolders: [], images: getImagesByFolderName("시간별", "시간3") }
            ] 
          }
        ],
      },
     
      // ... Other users and their subfolders
    ],
  },
  {
    name: "한양대에서😋",
    subfolders: [
      {
        name: "서혜인",
        subfolders: [
          { 
            name: "장소별", 
            subfolders: [
              { name: "사근동", subfolders: [], images: getImagesByFolderName("장소별", "장소1") },
              { name: "한양여자대학교", subfolders: [], images: getImagesByFolderName("장소별", "장소2") },
              { name: "한양대역", subfolders: [], images: getImagesByFolderName("장소별", "장소3") }
            ] 
          },
          { 
            name: "시간별", 
            subfolders: [
              { name: "20231207", subfolders: [], images: getImagesByFolderName("시간별", "시간1") },
              { name: "20231214", subfolders: [], images: getImagesByFolderName("시간별", "시간2") },
              { name: "20231221", subfolders: [], images: getImagesByFolderName("시간별", "시간3") }
            ] 
          }
        ],
      },
      {
        name: "용수진",  
        subfolders: [
          { 
            name: "장소별", 
            subfolders: [
              { name: "요코하마", subfolders: [], images: getImagesByFolderName("장소별", "장소1") },
              { name: "아키하바라", subfolders: [], images: getImagesByFolderName("장소별", "장소2") },
              { name: "사쿠라기초", subfolders: [], images: getImagesByFolderName("장소별", "장소3") }
            ] 
          },
          { 
            name: "시간별", 
            subfolders: [
              { name: "20231117", subfolders: [], images: getImagesByFolderName("시간별", "시간1") },
              { name: "20231118", subfolders: [], images: getImagesByFolderName("시간별", "시간2") },
              { name: "20231119", subfolders: [], images: getImagesByFolderName("시간별", "시간3") }
            ] 
          }
        ],
      },
     
      // ... Other users and their subfolders
    ],
  },
  {
    name: "잠실!",
    
  },
  // ... Other shared folders
];

const Categorize = () => {
  const navigate = useNavigate(); // useNavigate 훅 사용


  const handleImageClick = () => {
    // 이미지를 클릭했을 때 Edit.js 페이지로 이동
    navigate("/Edit");
  };

  const [selectedFolder, setSelectedFolder] = useState(null);
  const [currentPath, setCurrentPath] = useState([]);

  const handleFolderClick = (folder) => {
    setSelectedFolder(folder);
    
    // 클릭한 폴더의 이름을 현재 경로에 추가
    setCurrentPath((prevPath) => [...prevPath, folder.name]);
  };

  const handleTitleClick = () => {
    // 현재 경로에서 마지막 폴더 제거
    setCurrentPath((prevPath) => prevPath.slice(0, -1));
    // 선택된 폴더 초기화
    setSelectedFolder(null);
  };

  return (
    <CateContainer>
      <Header />
      <TitleWrap>
        {currentPath.length > 0 ? (
          <>
            {currentPath.map((folderName, index) => (
              <Title key={index} onClick={handleTitleClick}>
                📂&nbsp;{folderName}&nbsp;
                <FontAwesomeIcon
                  icon={faChevronRight}
                  style={{ color: "gray" }}
                />
              </Title>
            ))}
          </>
        ) : (
          <Title>📂&nbsp;공유 폴더&nbsp;</Title>
        )}
      </TitleWrap>

      <CateContents>
        <Container>
          {selectedFolder && selectedFolder.name === "잠실!" && (
            <FolderUploader />
          )}
          {selectedFolder && (
            <Imgshow2 images={getImagesByFolderName(selectedFolder.name)} onImageClick={handleImageClick} /> // 이미지 클릭 이벤트 핸들러 추가
          )}
          <FolderList
            folders={selectedFolder ? selectedFolder.subfolders || [] : folders}
            onFolderClick={handleFolderClick}
          />
        </Container>
      </CateContents>
    </CateContainer>
  );
};

export default Categorize;

const CateContainer = styled.div`
  display: flex;
  flex-direction: column;
  max-width: 100%;
  height: 150vh;
  background-color: ${oc.grape[0]};
`;

const CateContents = styled.div`
  max-width: 100%;
`;

const TitleWrap = styled.div`
  display: flex;
  flex-direction: row;
  width: 100%;
  text-align: center;
  align-items: center;

  margin: 0 auto;
  height: 10vh;
  padding-left: 25px;
  font-size: 18px;
  font-weight: bold;
  background-color: ${oc.blue[1]};
`;

const Title = styled.div`
  margin-left: 8px;
  flex-direction: row;
`;
