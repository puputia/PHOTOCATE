import React, { useEffect } from 'react';
import { Button } from 'react-bootstrap';
import KakaoLogo from '../assets/img/kakao.png';
import { useNavigate } from 'react-router-dom'; // 수정된 부분

const KakaoLogin = () => {
  const navigate = useNavigate(); // 수정된 부분

  useEffect(() => {
    // 카카오 SDK 초기화
    if (window.Kakao) {
      const initSuccess = window.Kakao.init('14700bc54118fa594a0e757ce25de03b');
      if (!initSuccess) {
        console.error('Failed to initialize Kakao SDK!');
      }
    } else {
      console.error('Kakao SDK not loaded!');
    }
  }, []);

  const handleKakaoLogin = () => {
    // 로그인 버튼 설정
    if (window.Kakao && window.Kakao.Auth) {
      window.Kakao.Auth.authorize({
        redirectUri: 'http://localhost:3000/oauth/login',
        success: function (authObj) {
          console.log('Successful login:', authObj);

          // 리다이렉션 성공 시 Home2로 이동
          navigate('/Home2'); // 수정된 부분
        },
        fail: function (err) {
          console.error('Failed to redirect:', err);
        },
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
