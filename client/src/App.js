import './App.css';
import React, { useState, useEffect} from 'react'
import PropertyForm from './components/PropertyForm';
import Map from './components/Map';
import LandingPage from './components/LandingPage';
import { SliderProvider } from './components/SliderProvider';
import Results from './components/Results';

function App() {

    return (
        <div>
            <LandingPage />
            <section id="property-form">
        <div className="app-container">
            <SliderProvider>
                <PropertyForm />
                <Map />
            </SliderProvider>
        </div>
        <div>
            <Results />
        </div>
        </section>
  </div>
);
}

export default App;
