import './App.css'
import Batsman from './Batsman';
import Counter from './Counter';

function App() {

  function handleClick(){
    alert('I am clicked')
  }

  const addnum=(num)=>{
    const newNum=num+5;
    alert(newNum);
  }

  return (
    <>
      
      <h1>Vite + React</h1>
      <Batsman></Batsman>
      <Counter></Counter>
      <button onClick={handleClick}>Click Me</button>
      <button onClick={() => addnum(10)}>add 5</button>
    </>
  )
}

export default App
