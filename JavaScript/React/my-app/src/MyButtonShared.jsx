import { useState } from "react";

// `export default` denotes the main component in the file.
export default function MyButtonShared() {
  // useState is a React Hook that lets you add state to function components.
  // Here, we declare a "count" state variable, initialized to 0.
  // We also get a "setCount" function that lets us update the count.
  // Calling setCount will re-render the component with the new count value.
  // Both buttons will share the same count state.
  const [count, setCount] = useState(0);

  function handleClick() {
    alert("You clicked me!");
    setCount(count + 1);
  }

  return (
    <div>
      <h2>These buttons will update together:</h2>
      <MyButton count={count} onClick={handleClick} />
      <br />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

function MyButton({ count, onClick }) {
  // className is used to apply CSS styles in React
  return (
    <button className="green-button" onClick={onClick}>
      Clicked {count} times
    </button>
  );
}
