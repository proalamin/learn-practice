import { useState } from "react"

export default function Batsman(){
    const [runs, setRuns] = useState(0)
    const [sixs, setSixs] = useState(0)

    return(
        <div>
            <h3>Player: Bangla Batsman</h3>
            <h1>Score: {runs}</h1>
            <h2>Total sixs: {sixs}</h2>
            <button onClick={()=> setRuns(runs+1)}>Single</button>
            <button onClick={()=> setRuns(runs+2)}>Double</button>
            <button onClick={()=> setRuns(runs+3)}>Triple</button>
            <button onClick={()=> setRuns(runs+4)}>Four</button>
            <button 
                onClick={()=>{
                    setRuns((prev)=> prev+6);
                    setSixs((prev)=> prev+1);
                
                }}>
            Six
            </button>

        </div>
    )
}