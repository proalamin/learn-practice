
const loadPost=()=>{
    const url='https://jsonplaceholder.typicode.com/posts/'
    
    fetch(url)
      .then((res) => res.json())
      .then((data) => display(data))
}

const display =(posts)=>{
    posts.forEach(post => {
        console.log(post)
    });
}