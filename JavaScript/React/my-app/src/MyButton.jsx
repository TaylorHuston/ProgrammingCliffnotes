import { useState } from "react";

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    alert("You clicked me!");
    setCount(count + 1);
  }

  // className is used to apply CSS styles in React
  return (
    <button className="pink-button" onClick={handleClick}>
      Clicked {count} times
    </button>
  );
}

// `export default` denotes the main component in the file.
export default function MyButtonComponent() {
  return (
    <div>
      <h2>This is a button component:</h2>
      <MyButton />
    </div>
  );
}
