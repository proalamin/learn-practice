import React, { use } from "react";
import Player from "../Player/Player";

const AvailablePlayers = ({ playerPromise }) => {
  const playerData = use(playerPromise);
  //   console.log(playerData);

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 my-8">
      {playerData.map((player) => (
        <Player key={player.id} player={player}></Player>
      ))}
    </div>
  );
};

export default AvailablePlayers;
