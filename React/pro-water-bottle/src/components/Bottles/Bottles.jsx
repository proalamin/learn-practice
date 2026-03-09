import React, { use, useEffect, useState } from "react";
import Bottle from "../Bottle/Bottle";
import "./Bottles.css";
import { addToStoredCart, getStoreCart } from "../../utilites/localstorage";

const Bottles = ({ bottlesPromise }) => {
  const [cart, setCart] = useState([]);

  const bottles = use(bottlesPromise);


  // useEffect
  useEffect(() => {
    // get the cart from local storage and set it to the state
    const storedCartIds = getStoreCart();
    console.log("stored cart", storedCartIds, bottles);
    // setCart(storedCart);

    const storedCart =[];

    for(const id of storedCartIds){
        // console.log(id);
        const cartBottle = bottles.find(bottle => bottle.id === id);
        // console.log(cartBottle);
        if(cartBottle){
            storedCart.push(cartBottle);
        }
    }
    if(storedCart.length > 0){
        setCart(storedCart);
    }




  }, [bottles]);   

  const handleAddToCart = (bottle) => {
    console.log("click", bottle);
    const newCart = [...cart, bottle];
    setCart(newCart);

    // save the bootle id in the storage
    addToStoredCart(bottle.id);


  };

  return (
    <div className="bottles">
      <h4 className="bottles-title">Total Bottles: {bottles.length}</h4>
      <h4 className="bottles-title">Total Cart Added: {cart.length}</h4>
      <div className="bottles-container">
        {bottles.map((bottle) => (
          <Bottle
            key={bottle.id}
            bottle={bottle}
            handleAddToCart={handleAddToCart}
          ></Bottle>
        ))}
      </div>
    </div>
  );
};

export default Bottles;
