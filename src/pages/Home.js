import React, { Component } from "react";
import styled from "styled-components";
// import oc from "open-color";
import "../App.css";
import Header from "../components/Header.js";
// import Footer from "../components/Footer.js";
import Carousel from "react-bootstrap/Carousel";
import Mosaic from "../assets/img/mosaic.png";
import Blur from "../assets/img/blur.png";
import BW from "../assets/img/blackwhite.png";
import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Button from "react-bootstrap/Button";
import Cat from "../assets/img/metadatacat.png";

import Logo from "../assets/Logo/pnglogo.png";

export class Home extends Component {
  render() {
    return (
      <>
        <Header />
        <HomeContainer>
          {/* <SlideBox> */}
          <Carousel slide={true} variant="dark">
            <Carousel.Item>
              <img
                className="rounded mx-auto d-block"
                src={BW}
                alt="logo img"
                style={{
                  maxWidth: "100%",
                  height: "600px",
                  alignItems: "center",
                }}
              />
            </Carousel.Item>
            <Carousel.Item>
              <img
                className="rounded mx-auto d-block"
                src={Mosaic}
                alt="logo img"
                style={{
                  maxWidth: "100%",
                  height: "600px",
                  alignItems: "center",
                }}
              />
            </Carousel.Item>
            <Carousel.Item>
              <img
                className="rounded mx-auto d-block"
                src={Blur}
                alt="logo img"
                style={{
                  maxWidth: "100%",
                  height: "600px",
                  alignItems: "center",
                }}
              />
            </Carousel.Item>
          </Carousel>
          {/* </SlideBox> */}
          <StepBox>
            <Intro>


              {/* 프로젝트 소개 */}
              <h1
                className="title"
                style={{
                  fontFamily: "PyeongChangPeace-Bold",
                  marginTop: "8vh",
                  padding: "2vh",
                }}
              >
                프로젝트 소개
              </h1>
              <div
                style={{
                  borderRadius: "50%",
                  height: "300px",
                  maxWidth: "300px",
                  backgroundColor: "white",
                  margin: "0 auto",
                }}
              >
                <img
                  src={Logo}
                  alt="logo img"
                  style={{
                    height: "180px",
                    marginTop: "6.5vh",
                    textAlign: "center",
                  }}
                />
              </div>
              <h3
                style={{
                  fontFamily: "MICEGothic Bold",
                  marginTop: "3vh",
                  color: "white",
                  marginBottom: "20vh",
                }}
              >
                PHOTOCATE는 사진분류와 사진편집을 편리하게 위해 고안된 사이트
                입니다.
              </h3>




              {/* 사진 분류 */}
              <h2 class="feature">&#91; 사진 분류&#93;</h2>
              <div style={{ fontFamily: "MICEGothic Bold" }}>
                GPS 기반의 장소, 시간 메타 데이터를 활용해 사진을 분류합니다
              </div>
              <img
                className="rounded mx-auto d-block"
                src={Cat}
                alt="logo img"
                style={{
                  maxWidth: "100%",
                  height: "50vh",
                  alignItems: "center",
                  margin: "10px",
                }}
              />
              <p>
                1. 포토 분류 페이지에 들어간다.
                <br />
                2. 한 사용자가 공유폴더를 만들고 이를 다른 사용자에게 공유한다
                <br />
                3. 만든 공유폴더 안에 공유된 사용자들이 이미지를 업로드한다.
                <br />
                4.장소에 따라 시간별로 사진이 분류된다.
                <br />
                5. 분류된 사진을 클릭해 확대 및 편집효과 적용이 가능하다.
              </p>



            {/* 사진편집 */}


              <h2 class="feature">&#91; 사진 편집&#93;</h2>
              <div style={{ fontFamily: "MICEGothic Bold" }}>
                모자이크, 블러, 색필터를 통해 사진을 편집 합니다
              </div>
              <img
                className="rounded mx-auto d-block"
                src={Cat}
                alt="logo img"
                style={{
                  maxWidth: "100%",
                  height: "50vh",
                  alignItems: "center",
                  margin: "10px",
                }}
              />
              <p>
                1. 포토 편집 페이지에 들어간다.
                <br />
                2. 사진을 업로드한 후 원하는 편집 아이콘을 누른다.
                <br />
                3. 모자이크, 블러, 색필터를 통해 사진을 편집 할 수 있다.
                <br />
                
              </p>

              {/* <Step
                style={{
                  width: "500px",
                  textAlign: "center",
                  alignItems: "center",
                  backgroundColor: "none",
                }}
              >
             
              </Step> */}

              {/* <PhotoEdit>
                  <Step
                    style={{
                      width: "650px",
                      marginRight: "100px",
                      backgroundColor: "white",
                    }}
                  >
                    <h4>사진편집 사용법</h4>
                    <p>
                      1. 사진 편집 페이지에 들어간다 <br />
                      2. 이미지를 가져올 방법을 선택한다(로컬 or 공유폴더){" "}
                      <br />
                      3. 선택한 방법으로 이미지를 가져온다 <br />
                      4. 이미지를 가져오면 바로 사진을 편집할 수 있는 페이지로
                      이동한다.
                    </p>
                  </Step>
                  <Card
                    style={{
                      width: "1000px",
                      textAlign: "left",
                      marginBottom: "10px",
                      marginRight: "100px",
                    }}
                  >
                    <Card.Header as="h3" style={{ fontWeight: "bold" }}>
                      Photo Edit
                    </Card.Header>
                    <Card.Body>
                      <Card.Text>
                        사진편집은 로컬과 공유폴더에서 이미지를 불러와 직접 사진
                        편집이 가능합니다
                      </Card.Text>
                      <Button variant="dark">바로가기</Button>
                    </Card.Body>
                  </Card>

                </PhotoEdit> */}
            </Intro>

            {/* <h2>사진분류</h2>
            <p>
              
              
              <button>공유폴더로 바로가기</button>
            </p>
            <h2>사진편집</h2>
            <p>
               <br />
              opencv 기술을 통해 모자이크, 블러, 색필터 처리가 가능합니다
            </p>
            */}
          </StepBox>
        </HomeContainer>
      </>
    );
  }
}

export default Home;

const HomeContainer = styled.div`
  dispaly: flex;
  flex-direction column;
  height: 30vh;
  background-color: white;
  max-width: 100%;
  justify-content : center;
  align-items:center;
  text-align: center;
`;

// const SlideBox = styled.div`
//   dispaly: flex;
//   flex-direction column;
//   height: 72.65vh;
//   background-color: ${oc.gray[3]}
//   max-width: 100%;

// `;

const StepBox = styled.div`
  dispaly: flex;
  flex-direction column;
  height: 1000vh;
  background-color: 	#BC8F8F;
  // max-width: 100%;
  
`;

const Intro = styled.div`
  dispaly: flex;
  flex-direction column;
  height: 800vh;
  background-color: #faacba;
  max-width: 100%;
  padding :30px;
`;

const Features = styled.div`
  width: 1000px;
  display: flex;
  flex-direction: Column;
  margin: 30px auto;
  align-items: left;
  text-align: center;
  height: 5000vh;
`;

const PhotoCategorize = styled.div`
  width: 1000px;
  display: flex;
  flex-direction: row;
  // margin: 0 auto;
  align-items: left;
  text-align: center;
  margin-bottom: 200px;
`;

const PhotoEdit = styled.div`
  //  width: 1000px;
  //   display:flex;
  //   flex-direction: row;
  //   // margin: 0 auto;
  //   align-items: right;
  //   text-align:right;
  //   margin-top:10px;
  width: 1000px;
  display: flex;
  flex-direction: row;
  // margin: 0 auto;
  align-items: left;
  text-align: center;
  margin-bottom: 200px;
`;

const Step = styled.div`
  display: flex;
  flex-direction: column;
  padding: "100%:";

  // const EditStep = styled.div
`;
// margin-right:"400px"
// `;
