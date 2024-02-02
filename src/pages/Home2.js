import React, { Component } from "react";
import styled from "styled-components";
// import oc from "open-color";
import "../App.css";
import Header from "../components/Header2.js";
import Footer from "../components/Footer.js";
import Carousel from "react-bootstrap/Carousel";
import Mosaic from "../assets/img/mosaic.png";
import Blur from "../assets/img/blur.png";
import BW from "../assets/img/blackwhite.png";

import Cat from "../assets/img/metadatacat.png";
import CategorizeStep from "../assets/img/CategorizeStep.png";
import EditStep from "../assets/img/EditStep.png";
import Logo from "../assets/Logo/pnglogo.png";
import Card from 'react-bootstrap/Card';



// filter 불러오기
import Origin from "../assets/img/Origin.jpg";
import BlurFilter from "../assets/img/BlurFilter.png";
import MosaicFilter from "../assets/img/MosaicFilter.png";
import Blue from "../assets/img/Blue.png";

export class Home2 extends Component {
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
              <div style={{ fontFamily: "MICEGothic Bold", margin: "15px"}}>
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
                 
                }}
              />
              <img
                className="rounded mx-auto d-block"
                src={CategorizeStep}
                alt="C-step"
                style={{
                  maxWidth: "100%",
                  height: "80vh",
                  alignItems: "center",
                  // margin: "-60px",
                }}
              />

              {/* 사진편집 */}
              <h2 class="feature">&#91; 사진 편집&#93;</h2>
              <div style={{ fontFamily: "MICEGothic Bold",margin:"15px" }}>
                모자이크, 블러, 색필터를 통해 사진을 편집 합니다
              </div>
              <CardBox>
                <Card className="bg-dark text-white" style={{width:"600px",height:"380px"}}>
                  <Card.Title style={{fontSize:"30px",fontFamily:"GoryeongStrawberry",margin:"10px auto"}}>원본</Card.Title>
                  <Card.Img src={Origin}  alt="Card image" />
                </Card>
                <Card className="bg-dark text-white" style={{width:"600px",height:"380px"}}>
                  <Card.Title style={{fontSize:"30px",fontFamily:"GoryeongStrawberry",margin:"10px auto"}}>모자이크</Card.Title>
                  <Card.Img src={MosaicFilter}  alt="Card image" />
                </Card>
                <br/>
                <Card className="bg-dark text-white" style={{width:"600px",height:"380px"}}>
                  <Card.Title style={{fontSize:"30px",fontFamily:"GoryeongStrawberry",margin:"10px auto"}}>블러</Card.Title>
                  <Card.Img src={BlurFilter}  alt="Card image" />
                </Card>
                <Card className="bg-dark text-white" style={{width:"600px",height:"380px"}}>
                  <Card.Title style={{fontSize:"30px",fontFamily:"GoryeongStrawberry",margin:"10px auto"}}>색필터(블루)</Card.Title>
                  <Card.Img src={Blue}  alt="Card image" />
                </Card>
              </CardBox>
              <img
                className="rounded mx-auto d-block"
                src={EditStep}
                alt="C-step"
                style={{
                  maxWidth: "100%",
                  height: "50vh",
                  alignItems: "center",
                }}
              />
            </Intro>
          </StepBox>
          <Footer />
        </HomeContainer>
      </>
    );
  }
}

export default Home2;

const HomeContainer = styled.div`
  dispaly: flex;
  flex-direction column;
  height: 10vh;
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

 
  
`;

const Intro = styled.div`
  dispaly: flex;
  flex-direction column;
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

const CardBox = styled.div`
  display: flex;
  flex-direction: row;
  
`;

