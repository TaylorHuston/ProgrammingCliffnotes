import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import MyButtonComponent from "./MyButton.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <MyButtonComponent />
  </StrictMode>
);
