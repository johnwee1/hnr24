import logo from "./logo.svg";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
import {
  Grid,
  Button,
  TextField,
  AppBar,
  Toolbar,
  Typography,
  Box,
} from "@mui/material";
import { ThemeProvider, useTheme } from "@mui/material/styles";
import Diff from "./Diff";

import Camera from "react-html5-camera-photo";
import "react-html5-camera-photo/build/css/index.css";

const ENDPOINT = "http://localhost:8000/ai/";
window.state = {};

function CameraUse(props) {
  const [info, setInfo] = useState({ textIdentified: "SinGaporE" });
  const [imageUri, setImageUri] = useState("");
  const [givenText, setGivenText] = useState("Singapore");
  const theme = useTheme();

  function handleTakePhoto(dataUri) {
    // Do stuff with the photo...
    console.log("takePhoto");
    setImageUri(dataUri);

    //alert(dataUri);
    fetch(dataUri)
      .then((response) => response.blob())
      .then((blob) => {
        const file = new File([blob], "sample.png", { type: blob.type });
        window.state.file = file;
        console.log(file); //File object
        //alert(file);
        return file;
      })
      .then((file) => {
        const formData = new FormData();
        formData.append("file", file);
        const fetchOptions = {
          method: "POST",
          body: formData,
        };

        fetch(ENDPOINT, fetchOptions)
          .then((response) => response.json())
          .then((data) => {
            setInfo(data);
          })
          .catch((err) => {
            alert(err);
            setInfo({ textIdentified: "test" });
          });
      });
  }

  const text = "the quick brown fox jump over the lazy dog";
  return (
    <Grid
      container
      direction="column"
      alignItems="center"
      justifyContent="center"
      style={{
        minHeight: "100vh",
        textAlign: "center",
        coloredBackground: {
          backgroundColor: "#00FF00",
          padding: "20px",
        },
      }}
    >
      {info === true ? (
        <div style={{ margin: 10 }}>
          <Typography align="center" variant="h3">
            Check your handwriting!
          </Typography>
          <Box
            display="flex"
            flexDirection="column"
            alignItems="center"
            justifyContent="center"
          >
            <Typography variant="body1">
              Text to write:{" "}
              <TextField
                type="text"
                value={givenText}
                onChange={(e) => setGivenText(e.target.value)}
              />
            </Typography>
          </Box>
          <Box width="100vw" height="100vw">
            <Camera
              onTakePhoto={(dataUri) => {
                handleTakePhoto(dataUri);
              }}
            />
          </Box>
        </div>
      ) : (
        <div style={{ margin: 10 }}>
          <Typography variant="h3">Feedback</Typography>
          {/* Find difference */}
          {/*JSON.stringify(info)*/}
          <p>{givenText}</p>
          <p>{info.textIdentified}</p>
          <Diff
            string2={givenText}
            string1={info.textIdentified}
            mode="characters"
          />
          <img src={imageUri}></img>
        </div>
      )}
    </Grid>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<CameraUse />} />
        <Route path="/about" element={<CameraUse />} />
        <Route path="/contact" element={<h1>Home</h1>} />
        <Route path="/blogs" element={<h1>blogs</h1>} />
        <Route path="/error" element={<h1>Error</h1>} />
      </Routes>
    </Router>
  );
}

export default App;
