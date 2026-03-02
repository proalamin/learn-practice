export default function Job({job}){

    return(
        <div className="card2">
            <h5>Title: {job.job_title}</h5>
            <p>company_name: {job.company_name}</p>
            <p>description: {job.description}</p>
        </div>
    )
}