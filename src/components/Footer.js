import React, { Component } from "react";
import styled from "styled-components";

import "../App.css";


export class Footer extends Component {
    render() {
      return (
        <FooterContainer>
            <Contents>
              ⓒ Copyright PhotoCate<br/> Github: https://github.com/Yongsoojin/capstone
              <br/>FE: 서혜인, BE: 용수진
            </Contents>
        </FooterContainer>
      );
    }
  }

export default Footer;
  
const FooterContainer = styled.div`
  max-width: 100%;
  background-color: black;
 
  display: flex;
  flex-direction: column;
  justify-content: bottom;
  height: 15vh;
`;

const Contents = styled.div`
  text-align: cneter;
  color: white;
  margin: auto 0;
`;
