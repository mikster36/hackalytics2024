//AIzaSyCzNRlt1SgsujvFDhEbiViRAG-glMzdXC8
import React, { useState, useEffect } from 'react';
import { Circle, GoogleMap, LoadScript, Marker } from '@react-google-maps/api';
import './Map.css';
import green_marker from '../resources/green_marker.png';
import { useSlider } from './SliderProvider';

const center = {
  lat: 33.7488,
  lng: -84.3877
};

const bounds = {
    north: 33.8, // Maximum latitude
    south: 33.7,  // Minimum latitude
    east: -84.32,  // Maximum longitude
    west: -84.455   // Minimum longitude
};

const mapOptions = {
    mapTypeControl: false,
    zoomControlOptions: {
      position: 9
    },
    streetViewControl: false,
    fullscreenControl: false,
    restriction: {
        latLngBounds: bounds,
        strictBounds: true // Set to true if you want to restrict panning to bounds only
      },
      clickableIcons: false,
      styles: [
        {
          featureType: 'poi.business',
          stylers: [
            { visibility: 'off' } // Hide all business-related POIs
          ]
        },
      ]
};

function Map() {
    const [mapClicked, setMapClicked] = useState(false);
    const { sliderValue, clickedPosition, onMapClick, houses, onCalculate } = useSlider();

    const handleMapClick = (event) => {
        if (!mapClicked) {
            const newPosition = {
                lat: event.latLng.lat(),
                lng: event.latLng.lng(),
              };
              // Update clicked position using the context
              onMapClick(newPosition);
            setMapClicked(true);
        }
    };


  console.log(houses)
    return (
        <div className='map-container'>
            <LoadScript
                googleMapsApiKey="AIzaSyCzNRlt1SgsujvFDhEbiViRAG-glMzdXC8"
            >
                <GoogleMap
                    mapContainerClassName='map'
                    center={center}
                    zoom={12}
                    options={mapOptions}
                    onClick={handleMapClick}
                >
                    {mapClicked && (
                        <>
                            <Marker position={clickedPosition} />
                            <Circle
                                center={clickedPosition}
                                radius={parseFloat(sliderValue)}
                                options={{
                                    strokeColor: "#FF0000",
                                    strokeOpacity: 0.8,
                                    strokeWeight: 2,
                                    fillColor: "#FF0000",
                                    fillOpacity: 0.35
                                }}
                            />
                        </>
                    )}
                    (houses !== null && {houses.map((house, index) => (
            <Marker
              key={index}
              position={{ lat: house.lat, lng: house.lng }}
            />
          ))})
                </GoogleMap>
            </LoadScript>
        </div>
    );
}

export default Map;
