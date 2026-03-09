import React from "react";

const Player = ({ player }) => {
  const { name, image, country, role, rating, battingStyle, price } = player;

  return (
    <div className="card bg-base-100 shadow-md rounded-2xl overflow-hidden">
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
          <span className="badge badge-outline">{role}</span>
        </div>
        <div className="divider my-1"></div>
        <p className="font-bold">Rating</p>
        <div className="flex items-center justify-between">
          <p className="font-bold">{battingStyle}</p>
          <p className="text-gray-500">{battingStyle}</p>
        </div>
        <div className="flex items-center justify-between mt-2">
          <p className="font-bold">Price: ${price}</p>
          <button className="btn btn-outline btn-sm rounded-lg">
            Choose Player
          </button>
        </div>
      </div>
    </div>
  );
};

export default Player;
