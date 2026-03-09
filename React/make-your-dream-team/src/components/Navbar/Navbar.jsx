import React from "react";

import logo from "../../assets/logo.png";
import coinIcon from "../../assets/Currency.png";

const Navbar = () => {
  return (
    <div className="navbar max-w-[1200px] flex items-center justify-between">
      <div className="flex-1">
        <a href="" className="text-xl">
            <img className="w-[60px] h-[60px]" src={logo} alt="Logo" />
        </a>
      </div>
      <div className="flex items-center">
        <span className="mr-1">600000</span>
        <span className="mr-1">Coins</span>
        <span>
          <img className="mr-1" src={coinIcon} alt="Coin" />
        </span>
      </div>
    </div>
  );
};

export default Navbar;
