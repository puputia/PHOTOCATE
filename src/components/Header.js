// Import 필요한 모듈
import React from "react";
import styled from "styled-components";
import { Link } from "react-router-dom";
import LogoImg from "../assets/Logo/pnglogo.png";
import "../App.css";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Profile from "../assets/user.png";

// Header 함수형 컴포넌트
const Header = () => {
  const handleLoginClick = () => {
    // 로그인 페이지로 이동하는 코드
    window.location.href = '/login'; // 적절한 경로로 변경
  };

  return (
    <HeaderWrapper>
      <Navbar bg="dark" variant="dark">
        <Container>
          <LogoBox>
            <img src={LogoImg} alt="logo img" height="35em" width="45em" />
          </LogoBox>
          <Navbar.Brand as={Link} to="/" style={{ fontFamily: "yg-jalnan" }}>
            PHOTOCATE 
          </Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/">Home</Nav.Link>
            <Nav.Link as={Link} to="/Categorize">Photo Categorize</Nav.Link>
            <Nav.Link as={Link} to="/Edit">Photo Edit</Nav.Link>
          </Nav>
          <Button style={{borderRadius:"20px"}} onClick={handleLoginClick}>
            <img src={Profile} alt="logo img" height="30em" width="30em" style={{margin:"5px auto"}} />
            &nbsp;로그인하기&nbsp;
          </Button>
        </Container>
      </Navbar>
    </HeaderWrapper>
  );
}

export default Header;
  
const HeaderWrapper = styled.div`
  
`;

const LogoBox = styled.div`
  margin-right: 8px;
`;

const Button = styled.div`
 background-color: white;
 width:120px;
 text-align:center;
`;

// 라우팅을 위한 부모 컴포넌트에서 BrowserRouter로 감싸야 합니다.
