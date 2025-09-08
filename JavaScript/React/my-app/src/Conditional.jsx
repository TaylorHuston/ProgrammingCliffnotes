export default function Conditional() {
  const isLoggedIn = true;
  let content;
  if (isLoggedIn) {
    content = "Admin Panel";
  } else {
    content = "Login Form";
  }

  return <div>{content}</div>;

  // Alternatively, you can use a ternary expression:
  // return <div>{isLoggedIn ? "Admin Panel" : "Login Form"}</div>;
}
