import React from 'react';
import './LandingPage.css'; // Import CSS file for styling

function LandingPage() {
    const handleScrollDown = () => {
        const section = document.getElementById('property-form'); // Change 'section10' to the ID of the section you want to scroll to
        section.scrollIntoView({ behavior: 'smooth' }); // Smooth scroll to the section
      };
      
 

  return (
    <div className='landing-page'>
        <div>
      <h1 className='heading'>realtor.ai</h1>
      <p className='sub-heading'>real estate investing simplified</p>
        </div>
        <div className="scroll-down">
        <a onClick={handleScrollDown}>
          <span></span>
        </a>
      </div>
    </div>
  );
}

export default LandingPage;
