import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import MyButtonComponent from "./MyButton.jsx";
import Profile from "./Profile.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <MyButtonComponent />
    <Profile />
  </StrictMode>
);
