function MyButton() {
  // className is used to apply CSS styles in React
  return <button className="pink-button">Click Me!</button>;
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
