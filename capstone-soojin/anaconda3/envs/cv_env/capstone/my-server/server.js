const { exec } = require('child_process');
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');
const app = express();
const port = 5000;

// 입력 매개변수를 파이썬에 전달 & 실행
app.use(bodyParser.json());

// CORS 미들웨어 추가
app.use(cors());

// 앱의 인코딩 설정(utf-8)
app.use((req, res, next) => {
    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    next();
})


app.post('/api/receivePythonResult', (req, res) => {
    // 요청에서 전달된 데이터
    const requestData = req.body;
    
    console.log('요청받은 데이터 값 : ', requestData);

    // 호출할 파이썬 경로 설정
    const pythonScriptPath = path.join(__dirname, '..', 'backend', 'user.py');

    // console.log('exec 문장 확인 : ', `python ${pythonScriptPath} ${requestData.param1} ${requestData.param2} ${requestData.param3}`)

    // 파이썬 스크립트 실행
    exec(`${pythonScriptPath} ${requestData.param1} ${requestData.param2} ${requestData.param3}`,
        (error, stdout, stderr) => {
            if (error) {
              // 명령어 실행 중 에러가 발생한 경우
                console.error(`Error: ${error.message}`);
                res.status(500).json({ error: 'Failed to call Python function' });
                return;
            }
            if(stderr) {
              // 명령어 실행 중 표준 에러 출력이 있는 경우
              console.error(`stderr : ${stderr}`);
              return;
            }
            // 명령어 실행 결과는 stdout에 저장되어 있음
            console.log(`Python script output: ${stdout}`);
            res.json({ result: 'Python function executed successfully', pythonOutput: stdout });
    });
});

// 자동 모자이크 처리
app.post('/filterButton', (req, res) => {
  try {
    // 클라이언트에서 보낸 데이터
    const filters = req.body;
    const filtervalue = Object.values(filters);
    let pythonOutput = ''

    pythonOutput = filters + ' 버튼이 클릭 되었습니다.';

    if (filtervalue == "mosaic_auto") {
      pythonOutput = '자동 모자이크 버튼이 클릭 되었습니다.';
    } else if (filtervalue == 'mosaic_not_auto') {
      pythonOutput = '수동 모자이크 버튼이 클릭 되었습니다.';
    } else if (filtervalue == 'blur_auto') {
      pythonOutput = '자동 블러 버튼이 클릭 되었습니다.';
    } else if (filtervalue == 'blur_not_auto') {
      pythonOutput = '수동 블러 버튼이 클릭 되었습니다.';
    } else if (filtervalue == 'color') {
      pythonOutput = '색 필터 버튼이 클릭 되었습니다.'
    }
    else {
      pythonOutput = 'Filter 버튼이 오류가 발생하였습니다.';
    }

    // 여기에서 모자이크 자동 처리 로직을 구현
    // requestData를 사용하여 이미지를 처리하고 결과를 얻음
    // const pythonOutput = '모자이크 처리 완료';

    // 클라이언트에 응답
    res.json({ pythonOutput });
  } catch (error) {
    console.error('Error:', error.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// 여러 개의 파이썬 파일 실행
// app.get('/api/callPythonScripts/manyPythonFile', (req, res) => {
//   const pythonFiles = ['../backend/filter.py', '../backend/getimag.py', '../backend/user.py'];

//   pythonFiles.forEach((pythonFile) => {
//     const pythonProcess = exec(`python ${pythonFile}`, (error, stdout, stderr) => {
//       if (error) {
//         console.error(`Error: ${error.message}`);
//         res.status(500).json({ error: `Failed to call ${pythonFile}` });
//         return;
//       }
//       console.log(`Python script output for ${pythonFile}: ${stdout}`);
//     });
//   });

//   res.json({ result: 'Python scripts executed successfully' });
// });

app.listen(port, () => {
  console.log(`Server is listening at http://localhost:${port}`);
});
