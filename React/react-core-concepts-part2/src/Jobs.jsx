import { use } from "react"
import Job from "./Job";

export default function Jobs({jobsPromise}){
    const jobs = use(jobsPromise);
    console.log(jobs);

    return(
        <div className="card">
            <h2>Jobs: {jobs.length}</h2>
            {
                jobs.map(job => <Job key={job.id} job={job}></Job>)
            }
        </div>
    )
}