import React, { Component } from 'react';
import { Link } from "react-router-dom";
import styled from "styled-components";
import oc from "open-color";
import "../App.css";
import "./Login.css";
import LogoImg from "../assets/Logo/pnglogo.png";
import LogoTit from "../assets/Logo/logotitle.png";
import KakaoLogo from "../assets/img/kakao.png";
import NaverLogo from "../assets/img/naver3.png";
import { Button } from 'react-bootstrap';

export class Login extends Component {
  render() {
    return (
      <LoginContainer>
        <LoginWrapper>
          <LoginContents>
            <LogoContainer>
              <ImgContainer>
                <Link to="/">
                  <img
                    src={LogoImg}
                    alt="logo img"
                    height="100em"
                    width="110em"
                  /></Link>
                  <Link to="/"><img src={LogoTit} alt="logo img" height="20em" /></Link>
                
              </ImgContainer>
              <ButtonGroup>
                <Link to="/Home2">
                  <Button
                    className="kakao-btn"
                    variant="warning mt-3"
                    size="lg"
                    style={{
                      background: "white",
                      border: "2px solid",
                      color: "black",
                      fontFamily: "Pretendard-Regular",
                      width: 300,
                      height: 60,
                      marginTop: "15px",
                      fontWeight: "bold",
                      borderRadius: "5px",
                      boxShadow: "2px 5px 8px #FEE500"
                    }}
                  >
                    <img
                      style={{
                        textAlign: "center",
                        border: "none",
                        width: "30px",
                        marginRight: "10px",
                      }}
                      src={KakaoLogo}
                      alt="카카오톡 로그인"
                    />
                    카카오로 로그인하기
                  </Button>
                </Link>

                <Link to="/Home2">
                  <Button
                    className="naver-btn"
                    variant="success mt-3"
                    size="lg"
                    style={{
                      background: "white",
                      border: "2px solid ",
                      color: "black",
                      fontFamily: "Pretendard-Regular",
                      width: 300,
                      height: 60,
                      marginTop: "15px",
                      fontWeight: "bold",
                      borderRadius: "5px",
                      boxShadow: "2px 5px 8px #06BE34"
                    }}
                  >
                    <img
                      style={{
                        textAlign: "center",
                        border: "none",
                        width: "28px",
                        marginRight: "13px",
                        marginBottom: "3px",
                        paddingLeft: "3px",
                      }}
                      src={NaverLogo}
                      alt="네이버 로그인"
                    />
                    네이버로 로그인하기
                  </Button>
                </Link>
              </ButtonGroup>
            </LogoContainer>
          </LoginContents>
        </LoginWrapper>
      </LoginContainer>
    );
  }
}

export default Login;

const LoginContainer = styled.div`
  disply: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  max-width: 100%;
  height: 100vh;
  background-color: black;
  padding-top: 80px;
`;

const LoginWrapper = styled.div`
  display: flex;
  flex-direction: column;
  justify-direction: center;
  text-align: center;
  align-items: center;
  margin: auto;
  border-radius: 15px;
  border-right: 3px solid #191970;
  border-bottom: 3px solid #191970;
  width: 450px;
  height: 600px;
  background: white;
`;

const LoginContents = styled.div`
  display: flex;
  justify-content: center;
  margin: 70px auto;
  font-size: 30px;
  max-width: 80%;
  height: 60vh;
`;

const LogoContainer = styled.div`
  display: flex;
  flex-direction: column;
`;

const ButtonGroup = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 5em;
`;

const ImgContainer = styled.div`
  display: flex;
  flex-direction: column;
  margin-top: 1em;
  margin-bottom: -2em;
  align-items: center;
`;
