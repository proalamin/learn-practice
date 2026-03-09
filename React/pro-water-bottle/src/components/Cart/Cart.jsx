import React from 'react';

const Cart = ({cart, handleRemoveFromCart}) => {

    return (
        <div>
            {
                cart.map(bottle=>
                    <div key={bottle.id}>
                        <img src={bottle.image} alt={bottle.name} width="50" />
                        <p>{bottle.name}</p>
                        <p>${bottle.price}</p>
                        <button onClick={()=> handleRemoveFromCart(bottle.id)}>X</button>
                    </div>
                )
            }
        </div>
    );
};

export default Cart;