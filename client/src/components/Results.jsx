import React from 'react';
import Tilt from 'react-parallax-tilt'
import './Results.css';
import house_img from '../resources/house.jpeg'

const results = {
    'house1' : {'address' : '311 S. Franklin Dr. Florence, SC ', 'price': '100,000', 'source_img': house_img, 'beds': 2, 'baths': 1, 'sqft': '1,002'},
    'house2' : {'address' : '311 S. Franklin Dr. Florence, SC', 'price': '200,000', 'source_img': house_img, 'beds': 2, 'baths': 1, 'sqft': '1,002'},
    'house3' : {'address' : '311 S. Franklin Dr. Florence, SC', 'price': '300,000', 'source_img': house_img, 'beds': 2, 'baths': 1, 'sqft': '1,002'},
    'house4' : {'address' : '311 S. Franklin Dr. Florence, SC', 'price': '300,000', 'source_img': house_img, 'beds': 2, 'baths': 1, 'sqft': '1,002'},
    // 'house5' : {'address' : '311 S. Franklin Dr. Florence, SC ', 'price': '100,000', 'source_img': house_img, 'beds': 2, 'baths': 1, 'sqft': '1,002'},
    // 'house6' : {'address' : '311 S. Franklin Dr. Florence, SC', 'price': '200,000', 'source_img': house_img, 'beds': 2, 'baths': 1, 'sqft': '1,002'},
    // 'house7' : {'address' : '311 S. Franklin Dr. Florence, SC', 'price': '300,000', 'source_img': house_img, 'beds': 2, 'baths': 1, 'sqft': '1,002'},
    // 'house8' : {'address' : '311 S. Franklin Dr. Florence, SC', 'price': '300,000', 'source_img': house_img, 'beds': 2, 'baths': 1, 'sqft': '1,002'},
}

const ResultCard = ({address, price, source_img, beds, baths, sqft}) => {
    return (
        <Tilt className="tilt" options={{
            max: 45,
            scale: 1,
            speed: 450
        }}>
        <div className='card'>
            <img src={source_img} alt={address} />
            <h1>${price}</h1>
            <p><strong> {beds} </strong> bds | <strong> {baths} </strong> ba | <strong>{sqft}</strong> sqft</p>
            <p>{address}</p>
        </div>
        </Tilt>
    )
} 

function Results() {
  return (
    <div className='results'>
        <div className='card_heading'>
        <h1>realtor.ai recommends...</h1>

        </div>
      <div className='card-container'>
        {Object.entries(results).map(([key, value]) => (
                        <ResultCard 
                        key={key}
                        address={value.address}
                        price={value.price}
                        source_img={value.source_img}
                        beds={value.beds}
                        baths={value.baths}
                        sqft={value.sqft}
                        />
                    ))}
      </div>
    </div>
  );
}

export default Results;
