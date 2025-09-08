import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import MyButtonComponent from "./MyButton.jsx";
import Profile from "./Profile.jsx";
import Conditional from "./Conditional.jsx";
import ShoppingList from "./Lists.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Conditional />
    <MyButtonComponent />
    <MyButtonComponent />
    <Profile />
    <ShoppingList />
  </StrictMode>
);
