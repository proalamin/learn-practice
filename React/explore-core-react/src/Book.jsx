
import './App.css'


export default function ({book}) {
  return (
    <div className="student">
      <h4>Name: {book.name}</h4>
      <p>Age: {book.price}</p>
    </div>
  );
}
