import { Suspense } from 'react';
import './App.css'
import Batsman from './Batsman';
import Counter from './Counter';
import Users from './Users';
import Friends from './Friends';
import Jobs from './Jobs';


// const fetchUser =fetch('https://jsonplaceholder.typicode.com/users')
//   .then(res=> res.json())

const fetchFriends= async() =>{
  const res = await fetch('https://jsonplaceholder.typicode.com/users');
  return res.json();
}


const fetchJobs= async() =>{
  const res = await fetch('https://uualamin.pythonanywhere.com/api/v1/jobs/');
  // const res = await fetch('http://127.0.0.1:8000/api/v1/jobs/')
  return res.json();
}

function App() {

  const friendsPromise = fetchFriends();
  const jobsPromise = fetchJobs();

  function handleClick(){
    alert('I am clicked')
  }

  const addnum=(num)=>{
    const newNum=num+5;
    alert(newNum);
  }

  return (
    <>
      
      {/* <h1>Vite + React</h1> */}

    <Suspense fallback={<h3>Jobs are loading....</h3>}>
      <Jobs jobsPromise={jobsPromise}></Jobs>
    </Suspense>

    {/* <Suspense fallback={<h3>Friends are coming......</h3>}>

      <Friends friendsPromise={friendsPromise}></Friends>

    </Suspense>


      <Batsman></Batsman>
      <Counter></Counter>
      <button onClick={handleClick}>Click Me</button>
      <button onClick={() => addnum(10)}>add 5</button> */}
    </>
  )
}

export default App
