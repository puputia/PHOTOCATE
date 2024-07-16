import Categorize from "./pages/Categorize.js";
import Home from "./pages/Home.js"
import ImgUpload from "./pages/ImgUpload.js";
import Login from "./components/Login.js";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import ImgShow2 from "./components/Imgshow2.js";
import PhotoEdit from "./pages/Edit.js";
import Home2 from "./pages/Home2.js";
import FolderImgUpload from "./components/FolderImgUpload.js";
import FolderUploader from "./components/FolderUploader.js";
import FileUpload from "./components/FileUpload.js";

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Home2" element={<Home2 />} />
        <Route path="/Categorize" element={<Categorize />} />
        <Route path="/FolderUpload" element={<FolderImgUpload />} />
        <Route path="/FolderUploader" element={<FolderUploader />} />
        {/* <Route path="/ImgUpload" element={<ImgUpload />} /> */}
        <Route path="/Edit" element={<ImgUpload />} />
        <Route path="/PhotoEdit" element={<PhotoEdit />} />
        <Route path="/Login" element={<Login />} />
        <Route path="/ImgShow2" element={<ImgShow2 />} />
        <Route path="/FileUpload" element={<FileUpload />} />
        <Route path="*" element={<h1>이 페이지는 없는 페이지 입니당</h1>} />
      </Routes>
    </div>
  );
}

export default App;