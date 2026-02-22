
import './App.css'
import Todo from './Todo'
import Actor from './actor'
import Singer from './singer'
import Library from './Library'


function App() {
  const actors = ['Bappa Raj', "Omar Synny", 'Salman Shah'];

  const singers =[
    {
      id:1,
      name: 'James',
      age:70
    },
    {
      id:2,
      name: 'Tahsan',
      age:50
    },{
      id:3,
      name: 'Xofar',
      age:30
    },
  ];

  const books =[
    {id: 1, name: 'Physics', price: 350},
    {id: 2, name: 'Chemistry', price: 300},
    {id: 3, name: 'Math', price: 330},
    {id: 4, name: 'Gk', price: 250},

  ]
  
  // const time=50;
  return (
    <>
      {/* <Todo task="learn react" isDone={true} time={time}></Todo>
      <Todo task="learn python" isDone={true} time={time}></Todo>
      <Todo task="learn DRF" isDone={false} time={time}></Todo> */}

      <Library books ={books}></Library>


      <h1>React Core concept</h1>
      {
        // actors.map(actor => <Actor actor={actor}></Actor>)
      }

      {
        singers.map(singer => <Singer  key={singer.id} singer={singer}></Singer>)
      }


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
