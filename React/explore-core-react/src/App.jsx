
import './App.css'
import Todo from './Todo'

function App() {
  const time=50;
  return (
    <>
      <Todo task="learn react" isDone={true} time={time}></Todo>
      <Todo task="learn python" isDone={true} time={time}></Todo>
      <Todo task="learn DRF" isDone={false} time={time}></Todo>

     
      <h1>React Core concept</h1>
      {/* <Student></Student>
      <Student></Student>
      <Person></Person>
      <Player name="sakib" runs='50000'></Player>
      <Player></Player> */}

    </>
  )
}


function Person(){
  const age= 17;

  const personStyle ={
    color: 'red'
  }
  return(
    <p style={personStyle}>I am a person , age is: {age}</p>

  )
}

// const {} ={name:"Sakib", runs}

function Player({name, runs}){
  console.log({name, runs})
  return(
    <div className='student'>
      <h3>Player name: {name}</h3>
      <p>Runs: {runs}</p>
    </div>
  )
}

function Student(){
  const name ="Al Amin";
  const age = 22;

  return(
    <div className='student'>
       <p>I am a Student and my name is {name}, age is {age}</p>
    </div>

  )
}
export default App
