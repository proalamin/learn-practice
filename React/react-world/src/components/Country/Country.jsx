import React, { useState } from 'react';
import './Country.css';

const Country = ({country, handleVisitedCountry, handleVisitedFlag}) => {
    // console.log(country);
    // console.log('handleVisitedCountry');

    const [visited, setVisited]= useState(false)

    const handleVisited=()=>{
        // if(visited){
        //     setVisited(false)
        // }else{
        //     setVisited(true)
        // }
        setVisited(visited ? false : true)

        handleVisitedCountry(country);
    };

    return (
        <div className={`country-card ${visited ? 'country-visited' : 'country-not-visited'}`}>
            <img
                className="country-flag"
                src={country.flags.flags.png}
                alt={country.flags.flags.alt}
            />
            <div className="country-content">
                <h3 className="country-name">Name: {country.name?.common}</h3>
                <p className="country-population">Population: {country.population.population}</p>
            </div>
            <button onClick={handleVisited}>
                {visited ? 'Visited' : 'Not Visited'}
            </button>
            <button onClickCapture={() =>{handleVisitedFlag(country.flags.flags.png)}}>Add Visited Flags</button>
            
        </div>
    );
};

export default Country;
