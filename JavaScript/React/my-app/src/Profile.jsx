const user = {
  name: "Hedy Lamarr",
  imageUrl: "https://i.imgur.com/yXOvdOSs.jpg",
  imageSize: 90,
};

export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img
        className="avatar"
        src={user.imageUrl}
        alt={"Photo of " + user.name}
        // The style attribute accepts a JavaScript object with camelCased properties rather than a CSS string.
        style={{
          width: user.imageSize,
          height: user.imageSize,
        }}
      />
    </>
  );
}
