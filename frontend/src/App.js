import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

function App() {
  return (
    <Router>
        <Routes>
            <Route exact path="/" element={<h1>Home</h1>} />
            <Route path="/about" element={<h1>about</h1>} />
            <Route
                path="/contact"
                element={<h1>Home</h1>}
            />
            <Route path="/blogs" element={<h1>blogs</h1>} />
            <Route
                path="/sign-up"
                element={<h1>Home</h1>}
            />
        </Routes>
    </Router>
  );
}

export default App;
