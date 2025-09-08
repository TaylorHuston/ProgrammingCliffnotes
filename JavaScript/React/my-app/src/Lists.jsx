const products = [
  { title: "Cabbage", isFruit: false, id: 1 },
  { title: "Garlic", isFruit: false, id: 2 },
  { title: "Apple", isFruit: true, id: 3 },
];

export default function Lists() {
  // Need to assign a key prop when creating lists of elements in React
  // so React can keep track of each element between renders.
  // The key should be a string or number that is unique among its siblings.
  // Here, we use the product ID, which is unique.
  // Do not use indexes as keys if the list can be reordered or changed.
  const listItems = products.map((product) => (
    <li
      key={product.id}
      style={{
        color: product.isFruit ? "magenta" : "darkgreen",
      }}
    >
      {product.title}
    </li>
  ));

  return <ul>{listItems}</ul>;
}
