const loadPost = () => {
    const url = "https://jsonplaceholder.typicode.com/posts";

    fetch(url)
        .then((res) => res.json())
        .then((data) => {
            // console.log(data);
            displayPosts(data);
        });
};

// {
//     "userId": 1,
//     "id": 2,
//     "title": "qui est esse",
//     "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
// }

const displayPosts = (posts) => {

    const postContainer = document.getElementById('post-container');
    postContainer.innerHTML='';

    posts.forEach((post) => {

        const postCard=document.createElement("div");
        postCard.innerHTML=`
         <div class="post-card">
            <h2>${post.title}</h2>
            <p>${post.body}</p>
        </div>

        `

        postContainer.append(postCard);
        // console.log(post);
    });

};


loadPost();