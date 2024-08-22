import React, { useState, useEffect } from 'react';
import image1 from './bannerimage.jpg';
// import image2 from '../../Cars/2LIEITC5GFLANTHEYTRDWAHRJU-cr-540.jpg';
// import image3 from '../../Cars/ALLEIKYKFBTRNXLWWSS3FCQJG4-cr-540.jpg';

function BannerImage({ image, active, caption }) {
  return (
    <div
      className={` inset-0 transition-opacity duration-1000 ease-in-out ${
        active ? 'opacity-100' : 'opacity-0'
      }`}
      style={{
        backgroundImage: `url(${image})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
      }}
    >
      <img src={image} alt={caption.title} className="w-full h-16 opacity-0" />
      <div className=" bottom-0 left-0 right-0 p-4 bg-black bg-opacity-50 text-white text-center">
        <h5 className="text-xl font-bold">{caption.title}</h5>
        <p>{caption.description}</p>
      </div>
    </div>
  );
}

const Banner = () => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const bannerImages = [image1];
  const bannerCaptions = [
    {
      title: "Welcome to Efo's Garage",
      description: "Special Offer: Get 10% off on all new arrivals!",
    },
    // {
    //   title: "Welcome to Efo's Garage",
    //   description: "Special Offer: Get 10% off on all new arrivals!",
    // },
    // {
    //   title: "Welcome to Efo's Garage",
    //   description: "Special Offer: Get 10% off on all new arrivals!",
    // },
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % bannerImages.length);
    }, 5000);

    return () => clearInterval(interval);
  }, [bannerImages.length]);

  return (
    <div className="flex-col justify-center text-white py-3 relative">
      {bannerImages.map((image, index) => (
        <BannerImage
          key={index}
          image={image}
          caption={bannerCaptions[index]}
          active={index === currentIndex}
        />
      ))}
      <div className="relative z-10 justify-center">
        <button>indicator</button>
      </div>
    </div>
  );
};

export default Banner;