const loadLessons = () => {
  fetch("https://openapi.programming-hero.com/api/levels/all")
    .then((res) => res.json())
    .then((data) => displayLessons(data.data));
};

const displayLessons = (lessons) => {
  const levelContainer = document.getElementById("level-container");
  levelContainer.innerHTML = "";

  for (let lesson of lessons) {
    const btnDiv = document.createElement("div");
    btnDiv.innerHTML = `
            <button id="lesson-btn-${lesson.level_no}" onclick="loadLevelWord(${lesson.level_no})" class="lesson-btn rounded border border-[#422ad5] px-4 py-2 text-sm font-semibold text-[#422ad5]">Lesson-${lesson.level_no}</button>
        `;
    levelContainer.append(btnDiv);
  }
};


const removeActive=()=>{
  const lesonBtn= document.querySelectorAll(".lesson-btn");
  lesonBtn.forEach((btn)=> btn.classList.remove("active"));
};

const loadLevelWord = (id) => {
  manageSpinner(true);
  // console.log(`id - ${id}`);
  const url = `https://openapi.programming-hero.com/api/level/${id}`;
  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      removeActive();
      const clickBtn=document.getElementById(`lesson-btn-${id}`);
      clickBtn.classList.add("active");
      displayLevelWorld(data.data);
    });
};


const displayLevelWorld = (words) => {
  const wordsContainer = document.getElementById("word-container");
  wordsContainer.innerHTML = "";

  if(words.length == 0){
    wordsContainer.innerHTML = `
      <div class="text-center col-span-full py-10 space-y-2">
                        <img class="mx-auto" src="./assets/alert-error.png" alt="">
                        <p class="font-bangla text-lg font-medium text-gray-500">এই Lesson এ এখনো কোন Vocabulary যুক্ত করা হয়নি।</p>
                        <h2 class="font-bangla text-4xl font-semibold">নেক্সট Lesson এ যান</h2>
                    </div>
    `;
    // alert("t");
    manageSpinner(false);

    return;
  }

  words.forEach((word) => {
    // console.log(word);
    const cardDiv = document.createElement("div");
    cardDiv.innerHTML = `
        <div class="space-y-4 rounded-xl bg-white px-4 py-10 text-center shadow-sm sm:px-5 md:py-12">
                        <h2 class="text-xl font-bold md:text-2xl">${word.word ? word.word : "শব্দ পাওয়া যায় নি"}</h2>
                        <p class="text-sm font-semibold text-zinc-500 md:text-base">Meaning / Pronounciation</p>
                        <div class="font-bangla text-xl font-medium text-zinc-600 md:text-2xl">"${word.meaning ? word.meaning : "আর্থ পাওয়া যায় নি" } / ${word.pronunciation ? word.pronunciation : "উচ্চারণ পাওয়া যায় নি"}"</div>
                        <div class="flex justify-between items-center">
                            <button onclick="loadWordDetails(${word.id})" class="btn-primary rounded-md bg-[#1A91FF40] px-3 py-2 hover:bg-[#1A91FF70] md:px-4">
                                <i class="fa-solid fa-circle-info"></i>
                            </button>
                            <button class="btn-primary rounded-md bg-[#1A91FF40] px-3 py-2 hover:bg-[#1A91FF70] md:px-4">
                                <i class="fa-solid fa-volume-high"></i>
                            </button>
                        </div>
                </div>
        `;
    wordsContainer.append(cardDiv);
  });

    manageSpinner(false);
};

const loadWordDetails = async(id) => {
  const url = `https://openapi.programming-hero.com/api/word/${id}`;
  const res = await fetch(url);
  const data = await res.json();

  console.log(data.data);
  disPlayWordDetails(data.data);
}; 

const disPlayWordDetails = (word) => {
  my_modal_5.showModal(word);
  const modalTitle = document.querySelector("#my_modal_5 .modal-box h3");
  const modalBody = document.querySelector("#my_modal_5 .modal-box p");

  modalTitle.innerText = word.word;
  modalBody.innerText = `Meaning: ${word.meaning} \n Pronunciation: ${word.pronunciation} \n Example:\n ${word.sentence
 ? word.sentence
 : "উদাহরণ পাওয়া যায় নি"}`;
};


const manageSpinner=(status)=>{
  if(status==true){
    document.getElementById("spiner").classList.remove("hidden");
    document.getElementById("word-container").classList.add("hidden");
  }else{
    document.getElementById("spiner").classList.add("hidden");
    document.getElementById("word-container").classList.remove("hidden");
  }
}
// {
//     "id": 5,
//     "level": 1,
//     "word": "Eager",
//     "meaning": "আগ্রহী",
//     "pronunciation": "ইগার"
// }

loadLessons();
