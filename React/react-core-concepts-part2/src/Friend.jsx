export default function Friend({friend}){
    console.log(friend)

    const {name, email, phone, website, address}= friend;

    return(
        <div className="card">
            <h4>Name: {name}</h4>
            <p>Email: {email}</p>
            <p>Phone: {phone}</p>
            <p>website: {website}</p>
            <p className="card2">address- street:{address.street}, suite:{address.suite}, city:{address.city}, zipcode:{address.zipcode}, geo- lat:{address.geo.lat}, lng:{address.geo.lng}</p>

        </div>
    )
}