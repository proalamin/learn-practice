
import { Suspense } from 'react'
import './App.css'
import Bottles from './components/Bottles/Bottles'

const bottlesPromise= fetch('../public/bottles.json')
  .then(res => res.json())


function App() {
  // const bottels_js=[
  //   {id:1, name: '1no bottel', price: 340, color: 'Black'},
  //   {id:2, name: '1no bottel', price: 340, color: 'Black'},
  //   {id:3, name: '1no bottel', price: 340, color: 'Black'},
  //   {id:4, name: '1no bottel', price: 340, color: 'Black'},
  //   {id:5, name: '1no bottel', price: 340, color: 'Black'},
  // ]




  return (
    <>
    
      <h1>It's pro water Bottle</h1>
      <Suspense fallback={<h3>Bottles are comming.....</h3>}>
        <Bottles bottlesPromise={bottlesPromise}></Bottles>
      </Suspense>
      
    </>
  )
}

export default App
