import React from "react";
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
  { name: "서혜인" },
  { name: "용수진" },
  { name: "에펠탑" },
  // 여러 폴더를 추가할 수 있습니다.
];



const Categorize = () => {
  return (
    <CateContainer>
      <Header />

      <TitleWrap>
        <Title>
          {/* 공유폴더 */}
          📂&nbsp;서울 여행&nbsp;
          <FontAwesomeIcon icon={faChevronRight} style={{ color: "gray" }} />
        </Title>
        {/* 사용자폴더 */}
        <Title>
          📂&nbsp;서혜인&nbsp;
          <FontAwesomeIcon icon={faChevronRight} style={{ color: "gray" }} />
        </Title>
        {/* 장소폴더 */}
        <Title>
          📂&nbsp;잠실&nbsp;
          <FontAwesomeIcon icon={faChevronRight} style={{ color: "gray" }} />
        </Title>
        {/* 시간폴더 */}
        <Title>
          📂&nbsp;20231011&nbsp;
          <FontAwesomeIcon icon={faChevronRight} style={{ color: "gray" }} />
        </Title>
      </TitleWrap>

      <CateContents>
        <Container>
          <FolderList folders={folders} />
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
