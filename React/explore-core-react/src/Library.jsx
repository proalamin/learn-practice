import Book from './Book'

export default function({books}){
    return(
        <div>
            <h2>Amin Library</h2>
            <p>Total Books: {books.length}</p>
            <ul>
                {
                    books.map(book => <Book key={book.id} book = {book}></Book>)
                }
            </ul>
        </div>
    )
}