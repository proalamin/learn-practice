import { Suspense } from "react";
import "./App.css";
import AvailablePlayers from "./components/AvailablePlayers/AvailablePlayers";
import Navbar from "./components/Navbar/Navbar";
import SelectedPlayers from "./components/SelectedPlayers/SelectedPlayers";

const fetchPlayers = async () => {
  const res = await fetch("/players.json");
  // console.log(res.json());
  return res.json();
};
// fetchPlayers()

function App() {
  const playerPromise = fetchPlayers();

  return (
    <>
      <div className="max-w-[1200px] mx-auto mx-auto px-4 py-2">
        <Navbar></Navbar>
        <Suspense
          fallback={<span className="loading loading-ring loading-lg"></span>}>
          <AvailablePlayers playerPromise={playerPromise}></AvailablePlayers>
        </Suspense>
        {/* <SelectedPlayers></SelectedPlayers> */}
      </div>
    </>
  );
}

export default App;
