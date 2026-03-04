import React, { use, useState } from 'react';
import Bottle from '../Bottle/Bottle';
import './Bottles.css';

const Bottles = ({ bottlesPromise }) => {


    const bottles = use(bottlesPromise);
    console.log(bottles);

    return (
        <div className="bottles">
            <h4 className="bottles-title">Total Bottles: {bottles.length}</h4>
            <div className="bottles-container">
                {bottles.map((bottle) => (
                    <Bottle key={bottle.id} bottle={bottle}></Bottle>
                ))}
            </div>
        </div>
    );
};

export default Bottles;
