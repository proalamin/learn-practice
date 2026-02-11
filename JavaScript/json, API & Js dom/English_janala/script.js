const loadLessons = () =>{
    fetch("https://openapi.programming-hero.com/api/levels/all")
        .then((res)=> res.json())
        .then((data) => displayLessons(data.data))
}

const displayLessons = (lessons) => {
    const levelContainer = document.getElementById("level-container");
    levelContainer.innerHTML="";

    for(let lesson of lessons){
        const btnDiv= document.createElement("div");
        btnDiv.innerHTML=`
            <button class="rounded border border-[#422ad5] px-4 py-2 text-sm font-semibold text-[#422ad5]">Lesson-${lesson.level_no}</button>
        `
        levelContainer.appendChild(btnDiv);
    }
}



loadLessons();