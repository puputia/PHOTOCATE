import Categorize from "./pages/Categorize.js";
import Home from "./pages/Home.js"
import ImgUpload from "./pages/ImgUpload.js";
import Login from "./components/Login.js";
// import ShareFolder from "./components/ShareFolder.js";
import { Routes, Route} from 'react-router-dom'
import "./App.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import ImgShow2 from "./components/Imgshow2.js";
import Edit from "./pages/Edit.js";
import Home2 from "./pages/Home2.js";
import FolderImgUpload from "./components/FolderImgUpload.js";
import FolderUploader from "./components/FolderUploader.js";
import FileUpload from "./components/FileUpload.js";

function App() {
  
  return (
    
    <div>
      <Routes>
        <Route path="/" element={ <Home/> } />
        <Route path="/Home2" element={ <Home2/> } />
        <Route path="/Categorize" element={ <Categorize/> } />
        <Route path="/FolderUpload" element={ <FolderImgUpload/> } />
        <Route path="/FolderUploader" element={ <FolderUploader/> } />
        <Route path="/Edit" element={ <ImgUpload/> } />
        <Route path="/Login" element={ <Login/> } />
        <Route path="/ImgShow2" element={ <ImgShow2/> } />
        <Route path="/FileUpload" element={ <FileUpload/> } />
        <Route path="*" element={ <h1>이 페이지는 없는 페이지 입니당</h1> } />
        {/* <Route path="/ImgUpload" element={ <ImgUpload/> } /> */}
      </Routes>


    {/* 이것저것 컴포넌트 */}
      {/* <ShareFolder/> */}
      {/* <Categorize /> */}
      {/* <Login/> */}
      {/* <Edit/> */}
      {/* <ImgUpload /> */}
      {/* <ImgShow/> */}
      {/* <Home/> */}
    </div>
  );
}

export default App;
