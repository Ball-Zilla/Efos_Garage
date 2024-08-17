import BannerZero from './Cullinan.jpg';
import BannerOne from './Hyundai.jpg';
import BannerTwo from './S-Class.jpg';
import React, { useState, useEffect, useCallback } from 'react';

const SLIDE_INTERVAL = 3000; // Slide interval set to 3 seconds

function BannerIndicator({ active, onClick }) {
  return (
    <button
      type="button"
      aria-current={active}
      aria-label={active ? 'Current Slide' : 'Change Slide'}
      className={`w-3 h-3 rounded-full ${active ? 'bg-black' : 'bg-gray-400'}`}
      onClick={onClick}
    />
  );
}

function BannerImage({ image, active, caption }) {
  return (
    <div
      className={`absolute inset-0 transition-opacity duration-1000 ease-in-out ${
        active ? "opacity-100" : "opacity-0"
      }`}
      style={{
        backgroundImage: `url(${image})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
      }}
    >
      <img src={image} alt={caption.title} className="w-full h-full object-cover" />
      <div className="absolute bottom-0 left-0 right-0 p-4 bg-black bg-opacity-50 text-white">
        <h5 className="text-xl font-bold">{caption.title}</h5>
        <p>{caption.description}</p>
      </div>
    </div>
  );
}

function Banner() {
  const [activeIndex, setActiveIndex] = useState(0);
  const banners = [
    { image: BannerZero, caption: { title: "Cullinan", description: "Cullinan Car" } },
    { image: BannerOne, caption: { title: "Hyundai", description: "Hyundai Luxury" } },
    { image: BannerTwo, caption: { title: "S Class", description: "Mercedes S-Class" } }
  ];

  const handleSlideChange = useCallback((index) => {
    setActiveIndex(index);
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      setActiveIndex((prevIndex) => (prevIndex + 1) % banners.length);
    }, SLIDE_INTERVAL);

    return () => clearInterval(interval);
  }, [banners.length]);

  return (
    <div className="relative w-full overflow-hidden" style={{ marginTop: "90px", height: "25vh" }}>
      <div className="absolute bottom-4 left-0 right-0 flex justify-center p-4 space-x-2 z-20">
        {banners.map((_, index) => (
          <BannerIndicator
            key={index}
            active={activeIndex === index}
            onClick={() => handleSlideChange(index)}
          />
        ))}
      </div>
      <div className="relative w-full h-full z-10">  {/* Ensure lower z-index */}
        {banners.map((banner, index) => (
          <BannerImage
            key={index}
            image={banner.image}
            active={activeIndex === index}
            caption={banner.caption}
          />
        ))}
      </div>
    </div>
  );
}

export default Banner;
