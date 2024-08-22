import Template from "./template/Template";
import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";  // Assuming you have these components
// import Products from "./components/Products";
// import Cart from "./components/Cart";
// import Checkout from "./components/Checkout";

function App() {
  return (
    <Template>
      <Routes>
        {/* <Route path="/products" element={<Products />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/checkout" element={<Checkout />} /> */}
        <Route path="/" element={<Home />} />
      </Routes>
    </Template>
  );
}

export default App;