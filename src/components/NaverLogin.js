import React from "react";
import NaverLogin from "react-naver-login";
import NaverLogo from "../assets/img/naver3.png";
import { Button } from 'react-bootstrap';

const NaverLoginButton = () => {
  const responseNaver = (res) => {
    console.log(res);
    // 로그인 성공 시 처리 로직을 추가합니다.
  };

  return (
    <NaverLogin
      clientId="YOUR_CLIENT_ID"
      callbackUrl="YOUR_CALLBACK_URL"
      onSuccess={responseNaver}
      onFailure={() => console.error("Naver login failed")}
      render={(props) => <YourCustomLoginButton onClick={props.onClick} />}
    />
  );
};

export default NaverLoginButton;

const YourCustomLoginButton = ({ onClick }) => {
  return (
    <Button
      onClick={onClick}
      className="naver-btn"
      variant="success mt-3"
      size="lg"
      style={{
        // background: "#06BE34",
        background: "white",
        border: "2px solid ",
        color: "black",
        fontFamily: "Pretendard-Regular",
        width: 300,
        height: 60,
        marginTop: "15px",
        fontWeight: "bold",
        borderRadius: "5px",
        boxShadow: "2px 5px 8px #06BE34",
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
        alt="카카오톡 공유"
      />
      네이버로 로그인하기
    </Button>
    //   <button onClick={onClick} style={{ /* Add your custom styles */ }}>
    //     네이버로 로그인
    //   </button>
  );
};
