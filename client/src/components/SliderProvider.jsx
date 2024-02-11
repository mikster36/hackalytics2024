import React, { createContext, useContext, useState } from 'react';

const SliderContext = createContext();

export const SliderProvider = ({ children }) => {
  const [sliderValue, setSliderValue] = useState(0);
  const [clickedPosition, setClickedPosition] = useState(null); // Add clicked position state
  const [houses, setHouses] = useState([])

  const onSliderChange = (value) => {
    setSliderValue(value);
  };

  const onMapClick = (position) => { // Function to update clicked position state
    setClickedPosition(position);
  };

  const onCalculate = (values) => {
    setHouses(values)
  }

  return (
    <SliderContext.Provider
      value={{
        sliderValue,
        onSliderChange,
        clickedPosition, 
        onMapClick,
        houses,
        onCalculate
      }}
    >
      {children}
    </SliderContext.Provider>
  );
};

export const useSlider = () => useContext(SliderContext);
