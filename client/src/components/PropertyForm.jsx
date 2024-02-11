import React, { useState } from 'react';
import './PropertyForm.css'
import { useSlider } from './SliderProvider';

function PropertyForm() {
  const [formData, setFormData] = useState({
    min_price: '',
    max_price: '',
    bedrooms: '',
    bathrooms: '',
    squareFeet: '',
    min_year: '',
    location: '',
  });
  const { sliderValue, onSliderChange, clickedPosition, houses, onCalculate} = useSlider()

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };
  const handleSliderChange = (e) => {
    onSliderChange(e.target.value);
    console.log(sliderValue)
  };


  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const postData = {
        min_price: formData.min_price,
        max_price: formData.max_price,
        bedrooms: formData.bedrooms,
        bathrooms: formData.bathrooms,
        squareFeet: formData.squareFeet,
        min_year: formData.min_year,
        location: formData.location,
        sliderValue: sliderValue,
        position: clickedPosition,
      };
  
      const response = await fetch('/submit-property', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
      });
      const response_houses = await fetch('/fetch-data');
      const data = await response_houses.json();
        onCalculate(data);
      if (response.ok) {
        console.log('Property submitted successfully!');
      } else {
        console.error('Failed to submit property');
      }
    } catch (error) {
      console.error('Error submitting property:', error);
    }
  };

  return (
    <div className="form-container">
      <h1>so, what are you looking for?</h1>
      <form onSubmit={handleSubmit}>
      <div className="form-group">
          <label>click the map for location !</label>
        </div>
        <div className="form-group">
          <label> distance - {sliderValue}m</label>
          <input type="range" name="sliderValue" min="0" max="5000" value={sliderValue} onChange={handleSliderChange} />
        </div>
        <div className="form-group">
          <label>min price</label>
          <input type="text" name="min_price" value={formData.min_price} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>max price</label>
          <input type="text" name="max_price" value={formData.max_price} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>bedrooms</label>
          <input type="text" name="bedrooms" value={formData.bedrooms} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>bathrooms</label>
          <input type="text" name="bathrooms" value={formData.bathrooms} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>square feet</label>
          <input type="text" name="squareFeet" value={formData.squareFeet} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>min year built</label>
          <input type="text" name="min_year" value={formData.min_year} onChange={handleChange} />
        </div>
  
        <button type="submit">submit</button>
    
      </form>
    </div>
  );
}

export default PropertyForm;



