import React, { Component } from "react";
import styled from "styled-components";
import oc from "open-color";
import "../App.css";
import Dropdown from "react-bootstrap/Dropdown";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import Button from "react-bootstrap/Button";
import DropdownButton from "react-bootstrap/DropdownButton";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearchMinus } from "@fortawesome/free-solid-svg-icons";
import { faSearchPlus } from "@fortawesome/free-solid-svg-icons";
import { faRedo } from "@fortawesome/free-solid-svg-icons";
import { faRotateLeft } from "@fortawesome/free-solid-svg-icons";

import { faCircleDown } from "@fortawesome/free-solid-svg-icons";
import { faDroplet } from "@fortawesome/free-solid-svg-icons";
import { faPalette } from "@fortawesome/free-solid-svg-icons";
import { faChessBoard } from "@fortawesome/free-solid-svg-icons";
import Photo from "../assets/love.png";
import Profile from "../assets/user.png";

import { useControls, TransformWrapper, TransformComponent } from "react-zoom-pan-pinch";
// import from "../style/Editstyle.css";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import { Link } from "react-router-dom";
import LogoImg from "../assets/Logo/pnglogo.png";
// 포토URL경로
// const Photo = "URL_OF_YOUR_PHOTO";

export class Edit extends Component {
  render() {
    const Controls = () => {
      const { zoomIn, zoomOut, resetTransform } = useControls();
      return (
        <>
          <Zoom>
            <Button onClick={() => zoomIn()}>
              <FontAwesomeIcon icon={faSearchPlus} /> Zoom In
            </Button>
            <Button onClick={() => zoomOut()}>
              <FontAwesomeIcon icon={faSearchMinus} /> Zoom Out
            </Button>
            <Button onClick={() => resetTransform()}>
              <FontAwesomeIcon icon={faRedo} /> Reset
            </Button>
          </Zoom>
        </>
      );
    };
    
    return (
      <EditWrapper>
        <Toolbar>
            <LogoContainer>
              <LogoBox>
                <img src={LogoImg} alt="logo img" height="35em" width="45em" />
              </LogoBox>
              <Navbar.Brand as={Link} to="/" style={{ fontFamily: "yg-jalnan" }}>
                PHOTOCATE 
              </Navbar.Brand>
            </LogoContainer>
            
            
        

          

          <FileName>
            <div style={{ margin: "auto", marginLeft: "31.5em", display:"flex", alignItems: "center", textAlign:"ceter" }}>
              kakaotalk202230505.jpg
            </div>
          </FileName>

          
        </Toolbar>
        <EditContents>
          <TransformWrapper>
          <Controls />
          <TransformComponent>
            <ImageArea>
            <img
              src={Photo}
              alt="logo img"
              width="100%"
            />
            </ImageArea>
          </TransformComponent>
          </TransformWrapper>
       
        </EditContents>
        <EditControl>
          <Mosaic>
            <Dropdown as={ButtonGroup}>
              <Button
                variant="gray"
                style={{
                  color: "white",
                  backgroundColor: "none",
                }}
              >
                <FontAwesomeIcon icon={faChessBoard} size="2x" />
                <div>모자이크</div>
              </Button>

              <Dropdown.Toggle split variant="dark" id="dropdown-split-basic" />

              <Dropdown.Menu>
                <Dropdown.Item href="#/action-1">자동 모자이크</Dropdown.Item>
                <Dropdown.Item href="#/action-2">수동 모자이크</Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown>
          </Mosaic>
          <Blur>
            <Dropdown as={ButtonGroup}>
              <Button
                variant="gray"
                style={{
                  // borderLeft: "0.1px  solid white",
                  // borderTop: "0.1px  solid white",
                  // borderBottom: "0.1px  solid white",
                  paddingleft: "10px",
                  color: "white",
                  backgroundColor: "none",
                }}
              >
                <FontAwesomeIcon icon={faDroplet} size="2x" />
                <div>블러</div>
              </Button>

              <Dropdown.Toggle split variant="dark" id="dropdown-split-basic" />

              <Dropdown.Menu>
                <Dropdown.Item href="#/action-1">자동 블러</Dropdown.Item>
                <Dropdown.Item href="#/action-2">수동 블러</Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown>
          </Blur>
          <ColorFilter>
                <Button variant="gray"  style={{paddingleft: "10px",
                  color: "white",
                  backgroundColor: "none"}}>
                  <FontAwesomeIcon icon={faPalette} size="2x" />
                  <div>색필터</div>
                  
                </Button>
                
           
          </ColorFilter>
        </EditControl>
      </EditWrapper>
    );
  }
}

export default Edit;

const EditWrapper = styled.div`
    display: flex;
    flex-direction: column;
    max-width: 100%
    height:100vh;
    background-color: ${oc.gray[9]};
    oveflow-x:hidden;
`;

// const EditContainer = styled.div`

// `;

const Toolbar = styled.div`
    display:flex;
    // justify-contents:center;
    flex-direction: row;
    color: white;
    text-align: center;
    
    max-width: 100%
    width: 500vh;
    height: 8vh;
    background-color: ${oc.gray[7]};
   
`;

const FileName = styled.div`
  display: flex;
  justify-contents: center;
  text-align: center;
`;

const ImageArea = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center; 
  margin: 58px auto;
  margin-left: 68vh;
  width: 50vh;
  max-height: 100%;

  background-color: ${oc.violet[3]};
`;

const EditContents = styled.div`
    max-width: 100%
    width: 280vh;
    height: 80vh;
     
    background-color: ${oc.gray[9]};

`;

const EditControl = styled.div`
    display:flex;
    flex-direction: row;
    max-width: 100%
    width: 500vh;
    height: 12vh;
    background-color: ${oc.gray[7]};
    color: white;
    text-align: center;
    align-items: center;
`;

const Zoom = styled.div`
  flex-direction: row;

  // margin: 20px auto;

  text-align: center;
  align-items: center;
`;



const Mosaic = styled.div`
  margin: 5px auto;
  flex-direction: column;
  border-radius: 8px;
`;

const Blur = styled.div`
  flex-direction: column;
  margin: 5px auto;

  border-radius: 8px;
`;

const ColorFilter = styled.div`
  flex-direction: column;
  margin: 5px auto;
`;


const LogoBox = styled.div`
  margin-right: 8px;
`;

const LogoContainer = styled.div`
  display:flex;
  flex-direction: row;
  align-items: center;
  padding: 1em;
  margin-left: 5em;
`;
