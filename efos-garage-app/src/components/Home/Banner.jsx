import BannerZero from './Cullinan.jpg';
import BannerOne from './Hyundai.jpg';
import BannerTwo from './S-Class.jpg';
import { useState } from "react";

// function BannerIndicator(props) {
//   return (
//     <button
//   type="button"
//   aria-current={props.active}
//   className={`w-3 h-3 rounded-full ${props.active ? 'bg-black' : 'bg-gray-400'}`}
//   onClick={() => handleSlide(props.index)} // Custom event handler
// />
//   )
// }

// function BannerImage (props) {
//   return (
//     <div className={`transition-opacity duration-1000 ease-in-out ${props.active ? 'opacity-100' : 'opacity-0 absolute'}`}
//     style={{ transition: "opacity 1s ease-in-out" }}
//     >
//       <div className='relative w-full' 
//       style={{paddingBottom: '56.25%', maxHeight: '400px'}}
//       >
//       <img src={props.image} className='d-block w-100 h-100 bg-blend-darken' alt='' />
//       </div>
//       <div className="absolute bottom-0 left-0 right-0 p-4 text-center hidden lg:block">
//         <h2 className="text-pretty text-2xl font-semibold">Welcome to Efo's Garage</h2>
//         <p className="text-gray-400">Your one-stop shop for all your automotive needs</p>
//       </div>
//     </div>
//   )
// }

function BannerIndicator({ active, onClick }) {
  return (
    <button
      type="button"
      aria-current={active}
      className={`w-3 h-3 rounded-full ${active ? 'bg-black' : 'bg-gray-400'}`}
      onClick={onClick}
    />
  );
}

function BannerImage({ image, active }) {
  return (
    <div
      className={`absolute inset-0 transition-opacity duration-1000 ease-in-out ${
        active ? "opacity-100" : "opacity-0"
      }`}
    >
      <img src={image} alt="Banner" className="w-full h-full object-cover" />
    </div>
  );
}

function Banner() {
  const [activeIndex, setActiveIndex] = useState(0);

  const banners = [BannerZero, BannerOne, BannerTwo];

  const handleSlideChange = (index) => {
    setActiveIndex(index);
  };

  return (
    <div className="relative w-full overflow-hidden" style={{ marginTop: "56px" }}>
      <div className="absolute bottom-0 left-0 right-0 flex justify-center p-4 space-x-2">
        {banners.map((_, index) => (
          <BannerIndicator
          key={index}
          active={activeIndex === index}
          onClick={() => handleSlideChange(index)}
        />
        
        ))}
      </div>
      <div className="relative w-full h-64">
        {banners.map((image, index) => (
          <BannerImage
            key={index}
            image={image}
            active={activeIndex === index}
          />
        ))}
      </div>
    </div>
  );
}

export default Banner;

