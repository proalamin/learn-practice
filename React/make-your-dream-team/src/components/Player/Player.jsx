import React from "react";

const Player = ({ player }) => {
  const { name, image, country, role, battingStyle, price } = player;

  return (
    <div className="card bg-white shadow-md rounded-2xl overflow-hidden border border-gray-200">
      <figure className="px-6 pt-6">
        <div className="w-full aspect-[4/3] overflow-hidden rounded-xl">
          <img src={image} alt={name} className="w-full h-full object-cover" />
        </div>
      </figure>
      <div className="card-body px-6 py-4">
        <h2 className="flex items-center gap-2 text-xl font-semibold">
          <span>👤</span> {name}
        </h2>
        <div className="flex items-center justify-between">
          <p className="flex items-center gap-2 text-gray-500">
            <span>🏴</span> {country}
          </p>
          <span className="badge border-gray-300 text-gray-600">{role}</span>
        </div>
        <div className="divider my-1"></div>
        <p className="font-bold">Rating</p>
        <div className="flex items-center justify-between">
          <p className="font-bold">{battingStyle}</p>
          <p className="text-gray-500">{battingStyle}</p>
        </div>
        <div className="flex items-center justify-between mt-2">
          <p className="font-bold">Price: ${price}</p>
          <button className="btn btn-sm rounded-lg btn-outline border-gray-300 text-gray-700 hover:bg-[#84B179] hover:text-white hover:border-[#84B179]">
            Choose Player
          </button>
        </div>
      </div>
    </div>
  );
};

export default Player;
