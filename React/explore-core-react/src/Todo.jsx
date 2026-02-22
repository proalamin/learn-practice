
// export default function ToDo({task,isDone}){
//     return(
//         <li>Task: {task}, status: {isDone}</li>
//     )
// }


// export default function ToDo({task,isDone}){
//     if(isDone){
//         return(
//             <li>Task: {task}</li>
//         )
//     }
//     else{
//         re
//     }
// }

// conditional rendering:
// condition ? true : false

// export default function ToDo({task, isDone, time=0}){
//     return(
//         isDone ? <li>Done: {task}</li> : <li>Not done: {task}</li>
//     )
// }


// conditional rendering: &&
// export default function ToDo({task, isDone, time=0}){
//     return(
//         isDone && <li>Done: {task} time:- {time}</li>
//     )
// }


// conditional rendering: ||
export default function ToDo({task, isDone, time=0}){
    return(
        isDone || <li>Not Done: {task}</li>
    )
}

