import { useState } from "react";

function MyButton() {
  // useState is a React Hook that lets you add state to function components.
  // Here, we declare a "count" state variable, initialized to 0.
  // We also get a "setCount" function that lets us update the count.
  // Calling setCount will re-render the component with the new count value.
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
