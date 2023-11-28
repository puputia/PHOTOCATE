import React, { useEffect } from 'react';
import { Button } from 'react-bootstrap';
import KakaoLogo from '../assets/img/kakao.png';

const KakaoLogin = () => {
  useEffect(() => {
    // 카카오 SDK 초기화
    if (window.Kakao) {
      window.Kakao.init('14700bc54118fa594a0e757ce25de03b'); // 여기에 REST API 키를 입력하세요
    } else {
      console.error('Kakao SDK not loaded!');
    }
  }, []);

  const handleKakaoLogin = () => {
    // 로그인 버튼 설정
    if (window.Kakao && window.Kakao.Auth) {
      window.Kakao.Auth.authorize({
        redirectUri: 'http://localhost:3000/oauth/login',
      });
    } else {
      console.error('Kakao SDK or Auth not available!');
    }
  };

  return (
    <div>
      <Button
        onClick={handleKakaoLogin}
        className="kakao-btn"
        variant="warning mt-3"
        size="lg"
        style={{
          background: 'white',
          border: '2px solid',
          color: 'black',
          fontFamily: 'Pretendard-Regular',
          width: 300,
          height: 60,
          marginTop: '15px',
          fontWeight: 'bold',
          borderRadius: '5px',
          boxShadow: '2px 5px 8px #FEE500',
        }}
      >
        <img
          style={{
            textAlign: 'center',
            border: 'none',
            width: '30px',
            marginRight: '10px',
          }}
          src={KakaoLogo}
          alt="카카오 로그인"
        />
        카카오로 로그인하기
      </Button>
    </div>
  );
};

export default KakaoLogin;