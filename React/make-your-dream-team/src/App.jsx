import { Suspense, useState } from "react";
import "./App.css";
import AvailablePlayers from "./components/AvailablePlayers/AvailablePlayers";
import Navbar from "./components/Navbar/Navbar";
import SelectedPlayers from "./components/SelectedPlayers/SelectedPlayers";

const fetchPlayers = async () => {
  const res = await fetch("/players.json");
  // console.log(res.json());
  return res.json();
};


function App() {
  const [toggle, setToggle]=useState(true);

  const playerPromise = fetchPlayers();

  return (
    <>
      <div className="max-w-[1200px] mx-auto mx-auto px-4 py-2">
        <Navbar></Navbar>

        <div className="flex justify-between items-center my-6">
          <h1 className="text-2xl font-bold">Available Players</h1>
          <div className="border border-gray-300 rounded-full overflow-hidden flex">
            <button onClick={()=>setToggle(true)} className={`px-5 py-2 font-semibold rounded-full ${toggle===true? 'bg-yellow-300' : ''}`}>Available</button>
            <button onClick={()=>setToggle(false)} className={`px-5 py-2 font-semibold rounded-full ${toggle===true? '' : 'bg-yellow-300'}`}>Selected (0)</button>
          </div>
        </div>

        {
          toggle === true? 
            <Suspense
            fallback={<span className="loading loading-ring loading-lg"></span>}>
            <AvailablePlayers playerPromise={playerPromise}></AvailablePlayers>
            </Suspense>
          :
          <SelectedPlayers></SelectedPlayers>
        }

        


        
      </div>
    </>
  );
}

export default App;
