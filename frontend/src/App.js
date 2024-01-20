import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import {useState} from 'react';

import Camera from 'react-html5-camera-photo';
import 'react-html5-camera-photo/build/css/index.css';

const ENDPOINT = "http://localhost:8000/ai/";
window.state = {};

function CameraUse (props) {
  const [info, setInfo] = useState(false) ;
  const [imageUri, setImageUri] = useState("");
  const [givenText, setGivenText] = useState("");

  function handleTakePhoto (dataUri) {
    // Do stuff with the photo...
    console.log('takePhoto');
    setImageUri(dataUri);

    alert(dataUri);
    fetch(dataUri)
    .then(response => response.blob())
    .then(blob => {
        const file = new File([blob], "sample.png", {type: blob.type})
        window.state.file = file;
        console.log(file);    //File object
        alert(file);
        return file
    }).then(file => {
      const formData = new FormData();
        formData.append("file",file);
        const fetchOptions = {
          method: "POST",
          body: formData,
        };
        
        fetch(ENDPOINT, fetchOptions)
        .then(response => response.json())
        .then((data) => {
          setInfo(data);
        })
        .catch((err)=>{
          alert(err);
          setInfo({"textIdentified":"test"});
        });
    })
  }

  const text = "the quick brown fox jump over the lazy dog";
  return (
    <>
      {
        info === false ? 
        <div style={{"margin": 10}}>
          <h1>Take a photo of handwriting!</h1>
          <p>Text to write: <input value={givenText} onChange={(e) => setGivenText(e.target.value)}></input></p>
          <Camera
            onTakePhoto = { (dataUri) => { handleTakePhoto(dataUri); } }
          />
        </div>
        :
        <div style={{"margin": 10}}>
          <h1>Feedback</h1>
          {/* Find difference */}
          {/*JSON.stringify(info)*/}
          <p>{givenText}</p>
          <p>{info.textIdentified}</p>
          <img src={imageUri}></img>
        </div>
      }
    </>
  );
}


function App() {
  return (
    <Router>
        <Routes>
            <Route exact path="/" element={<CameraUse/>} />
            <Route path="/about" element={<CameraUse/>} />
            <Route path="/contact" element={<h1>Home</h1>}/>
            <Route path="/blogs" element={<h1>blogs</h1>}/>
            <Route path="/error" element={<h1>Error</h1>}/>
        </Routes>
    </Router>
  );
}

export default App;
