import React from 'react';
import './Bottle.css';

const Bottle = ({ bottle }) => {
    const { name, brand, capacity, color, material, weight, usageDuration, waterType, price, image } = bottle;
    const colorMap = {
        Silver: '#b7bcc6',
        Blue: '#2f80ed',
        Transparent: '#dce8f6',
        Black: '#1f1f1f',
        Green: '#2f9e44',
    };
    const swatchColor = colorMap[color] || '#9aa0a6';

    return (
        <div className="bottle-card">
            <div className="bottle-image-wrap">
                <img className="bottle-image" src={image} alt={name} />
                <span className="bottle-chip bottle-chip-type">{waterType}</span>
            </div>

            <div className="bottle-head">
                <h4 className="bottle-name">{name}</h4>
                <p className="bottle-brand">{brand}</p>
            </div>

            <div className="bottle-highlights">
                <span className="bottle-chip">{capacity}</span>
                <span className="bottle-chip">{material}</span>
                <span className="bottle-chip">{weight}</span>
            </div>

            <div className="bottle-details">
                <p><span>Usage</span><strong>{usageDuration}</strong></p>
                <p>
                    <span>Color</span>
                    <strong className="bottle-color">
                        <span className="bottle-swatch" style={{ backgroundColor: swatchColor }}></span>
                        {color}
                    </strong>
                </p>
            </div>

            <div className="bottle-actions">
                <p className="bottle-price">
                    <span>Price</span>
                    <strong>${price.toFixed(2)}</strong>
                </p>
                <button className="buy-btn" type="button">Buy Now</button>
            </div>
        </div>
    );
};

export default Bottle;
