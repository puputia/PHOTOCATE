// Categorize.js

import React, { useState } from "react";
import styled from "styled-components";
import oc from "open-color";
import "../App.css";
import Container from "react-bootstrap/Container";

import FolderList from "../components/FolderList";
import Header from "../components/Header.js";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Button from "react-bootstrap/Button";
import { faChevronRight } from "@fortawesome/free-solid-svg-icons";

const folders = [
  {
    name: "서혜인",
    subfolders: [
      { name: "장소별", subfolders: [{ name: "시간별", subfolders: [] }] },
    ],
  },
  {
    name: "용수진",
    subfolders: [
      { name: "장소별", subfolders: [{ name: "시간별", subfolders: [] }] },
    ],
  },
  {
    name: "송강",
    subfolders: [
      { name: "장소별", subfolders: [{ name: "시간별", subfolders: [] }] },
    ],
  },
  // 필요에 따라 더 많은 폴더 및 서브폴더를 추가하세요.
];

const Categorize = () => {
  const [selectedFolder, setSelectedFolder] = useState(null);
  const [currentPath, setCurrentPath] = useState([]);

  const handleFolderClick = (folder) => {
    setSelectedFolder(folder);

    // 클릭한 폴더의 이름을 현재 경로에 추가
    setCurrentPath((prevPath) => [...prevPath, folder.name]);
  };

  return (
    <CateContainer>
      <Header />

      <TitleWrap>
        {currentPath.length > 0 ? (
          <>
            {currentPath.map((folderName, index) => (
              <Title key={index}>
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
