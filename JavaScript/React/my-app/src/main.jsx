import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import MyButtonComponent from "./MyButton.jsx";
import Profile from "./Profile.jsx";
import Conditional from "./Conditional.jsx";
import MyButtonShared from "./MyButtonShared.jsx";
import Board from "./TicTacToe.jsx";
import Lists from "./Lists.jsx";
import Game from "./TicTacToe.jsx";
import ShoppingList from "./ShoppingList.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    {/* <Conditional />
    <MyButtonComponent />
    <MyButtonShared />
    <Profile />
    <Lists />
    <App /> 
    <Game /> */}
    <ShoppingList />
  </StrictMode>
);
