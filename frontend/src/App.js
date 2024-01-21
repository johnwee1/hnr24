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

import Camera, { FACING_MODES, IMAGE_TYPES } from "react-html5-camera-photo";
import "react-html5-camera-photo/build/css/index.css";

const ENDPOINT = "http://localhost:8000/ai/";
window.state = {};

function CameraUse(props) {
  const [info, setInfo] = useState(false);
  const [imageUri, setImageUri] = useState("");
  const [givenText, setGivenText] = useState("");
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
            //setInfo({ textIdentified: "test", suggestion: "suggestion" });
          });
      });
  }

  const text = "the quick brown fox jump over the lazy dog";
  return (
    <Grid
      container
      direction="column"
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
      {info === false ? (
        <div style={{ margin: 10}}>
          <Typography align="center" variant="h4">
            Check your handwriting!
          </Typography>
          <Box
            display="flex"
            flexDirection="row"
            alignItems="center"
            justifyContent="center"
          >
            <Typography variant="body1">
              Text to write:{" "}
              <br/>
              <TextField
                type="text"
                value={givenText}
                onChange={(e) => setGivenText(e.target.value)}
              />
            </Typography>
          </Box>
          <br/>
          <Box width="100%" height="80vw">
            <Camera
              idealFacingMode={FACING_MODES.ENVIRONMENT}
              onTakePhoto={(dataUri) => {
                handleTakePhoto(dataUri);
              }}
            />
          </Box>
        </div>
      ) : (
        <div style={{ margin: 10, width:"100vw" }}>
          <Typography variant="h3">Feedback</Typography>
          <p>{`What you wrote: ${info.textIdentified}`}</p>
          <p>{`The correct spelling: ${givenText ? givenText : info.suggestion.replace("The correct spelling: ", "")}`}</p>
          <Diff
            string2={givenText ? givenText : info.suggestion.replace("The correct spelling: ", "")}
            string1={info.textIdentified}
            mode="characters"
          />
          {
            givenText 
            ? 
            <p>{`Suggestion for you: ${info.suggestion.replace("The correct spelling: ", "")}`}</p>
            :
            <></>
          }
          <p></p>
          <img src={imageUri}></img>
          <br/>
          <Button
            variant="outlined"
            onClick={()=>{setInfo(false);}}
          >
            Back
          </Button>
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
