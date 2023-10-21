import React, { Component } from "react";
import styled from "styled-components";
import oc from "open-color";
import "../App.css";

import Header from "../components/Header.js";
// import Folder from "../assets/Folder.png";
import Local from "../assets/Local.png";

// import { Button } from "react-bootstrap";


class ImgUpload extends Component {
  render() {
    return (
      <UploadContainer>
        <Header />
        <Title>포토편집</Title>
        <SubTitle>편집할 사진을 업로드 해주세요</SubTitle>
        <Upload>
          <LocalUpload>
            <img
              src={Local}
              alt="logo img"
              style={{ width: "15em", margin: "30px auto" }}
            />
            <BtnStyle>
              {/* 로컬 파일 불러오기 직관적 버튼 */}
              {/* <label htmlFor="ex_file">
                <div className="btnStart" style={{border:"none", backgroundColor:"purple",fontSize:"15px", borderRadius:"30px",padding:"20px"}}>
                  로컬 파일 불러오기
                </div>
              </label> */}

              {/* 파일 선택 + 파일명 나오는 버튼 추후 서버 연동 알아 본후 연결하기 */}
              <input
                type="file"
                id="ex_file"
                accept="image/jpg, image/png, image/jpeg"
                onChange={(e) => console.log(e.target.files[0])}
                style={{ width: "15em", margin: "5px auto",marginLeft:"45px",  }}
              />
            </BtnStyle>
            
            {/* <input type="file" id="input-file" style={{ display: "none" }} /> */}
{/*            
            <input
              type="file"
              accept="image/jpg, image/png, image/jpeg"
              onChange={(e) => console.log(e.target.files[0])}
            /> */}
           
          </LocalUpload>
          {/* 
          <ShareUpload>
            <img
              src={Folder}
              alt="logo img"
              style={{ width: "15em", margin: "30px auto" }}
            />
            <Button
              style={{
                display: "flex",
                justifyContent: "center",
                borderRadius: "30px",
                width: "10em",
                alignItems: "center",
                textAlign: "center",
                margin: "auto",
              }}
            >
              공유폴더에서 열기
            </Button>
          </ShareUpload> */}
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
    height:150vh;
    background-color: ${oc.grape[0]}
    
`;

const Title = styled.div`
  text-align: center;
  align-items: center;
  margin: 0 auto;
  padding-top: 45px;
  font-weight: bold;
  font-size: 30px;
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

const LocalUpload = styled.div`
  width: 400px;
  height: 500px;
  background-color: pink;

  padding-top: 50px;
`;

// const ShareUpload = styled.div`
//   width: 400px;
//   height: 500px;
//   background-color: #deabde;
//   padding-top: 50px;
// `;

const BtnStyle = styled.div`
  flex-direction: column;
  margin: 0 auto;
  padding: 10px;
  // margin: 0 8px 0 8px;
  // color:white;
  // font-weight: semi-bold;
  // label {
  //   display: inline-block;
  //   font-size: inherit;
  //   line-height: normal;
  //   vertical-align: middle;
  //   cursor: pointer;
  // }
  // input[type="file"] {
  //   position: absolute;
  //   width: 0;
  //   height: 0;
  //   padding: 0;
  //   margin: -1px;
  //   overflow: hidden;
  //   clip: rect(0, 0, 0, 0);
  //   border: 0;
  // }
`;