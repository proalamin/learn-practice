import React, { use, useState } from 'react';
import Bottle from '../Bottle/Bottle';
import './Bottles.css';

const Bottles = ({ bottlesPromise }) => {
    const [cart, setCart] = useState([]);
    
    const bottles = use(bottlesPromise);

    const handleAddToCart = (bottle)=>{
        console.log('click', bottle)
        const newCart =[...cart, bottle];
        setCart(newCart);
    }

    return (
        <div className="bottles">
            <h4 className="bottles-title">Total Bottles: {bottles.length}</h4>
            <h4 className="bottles-title">Total Cart Added: {cart.length}</h4>
            <div className="bottles-container">
                {bottles.map((bottle) => (
                    <Bottle key={bottle.id} bottle={bottle} handleAddToCart={handleAddToCart}></Bottle>
                ))}
            </div>
        </div>
    );
};

export default Bottles;
