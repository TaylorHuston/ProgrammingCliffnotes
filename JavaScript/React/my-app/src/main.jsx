import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import MyButtonComponent from "./MyButton.jsx";
import Profile from "./Profile.jsx";
import Conditional from "./Conditional.jsx";
import ShoppingList from "./Lists.jsx";
import MyButtonShared from "./MyButtonShared.jsx";
import Board from "./TicTacToe.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Conditional />
    <MyButtonComponent />
    <MyButtonShared />
    <Profile />
    <ShoppingList />
    <Board />
    <App />
  </StrictMode>
);
