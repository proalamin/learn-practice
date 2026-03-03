import React, { use, useState } from 'react';
import Country from '../Country/Country';
import './countries.css';

const Countries = ({countriesPromise}) => {

    const [visitedCountries, setVisitedCountries] = useState([]);
    const [visitedFlags, setVisitedFlags] = useState([]);


    const handleVisitedCountry = (country)=>{
        // console.log('visited count', country)
        const newVisited = [...visitedCountries, country];
        setVisitedCountries(newVisited);
    }

    const handleVisitedFlag=(flag)=>{
       const newVisitedFlag= [...visitedFlags, flag];
       setVisitedFlags(newVisitedFlag);
    }

    const countriesData = use(countriesPromise);
    const countries = countriesData.countries;

    return (
        <section className='countries-section'>
            <h3 className="countries-title">Countries: {countries.length}</h3>
            <h4>Total Visited county: {visitedCountries.length}</h4>
            <h4>Total Visited county flags: {visitedFlags.length}</h4>

            <div>
                {
                    visitedFlags.map((flag, index) =><img key={index} src={flag}></img>)
                }
            </div>

            <div className="countries-grid">
                {
                    countries.map(country => <Country key={country.cca3.cca3} country={country} handleVisitedCountry={handleVisitedCountry} handleVisitedFlag={handleVisitedFlag}></Country>)
                }
            </div>
        </section>
    );
};

export default Countries;
