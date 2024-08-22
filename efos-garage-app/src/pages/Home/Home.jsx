import Banner from "../../Components/Banner";
// import FeatureProduct from "../../Components/FeatureProduct/FeatureProduct";
import ScrollToTopOnMount from "../../template/ScrollToTopOnMount";
import React from "react";
import { Link } from "react-router-dom";
// import Image1 from "../../Cars/B6VTQBN72BWQLQO6WXKGXQGM24-cr-540.jpg";
// import Image2 from "../../Cars/2LIEITC5GFLANTHEYTRDWAHRJU-cr-540.jpg";
// import Image3 from "../../Cars/ALLEIKYKFBTRNXLWWSS3FCQJG4-cr-540.jpg";

function Home() {
      // const [products, setProducts] = useState([]);

      // useEffect(() => {
      //   // Fetch data from the API
      //   fetch("https://api.api-ninjas.com/v1/cars?limit=2&model=camry", {
      //     headers: { "X-Api-Key": "NA'M3FlTDlaJqiy5p2OCDRX9A==1tOK0kIbNJNhKFIm'NA" }
      //   })
      //     .then(response => response.json())
      //     .then(data => {
      //       // Set the fetched data to state
      //       setProducts(data);
      //     })
      //     .catch(error => console.error("Error fetching the car data:", error));
      // }, []);
  return (
    <>
      <ScrollToTopOnMount />
      <Banner />
      <div className="flex flex-col bg-white py-4">
        <p className="text-center px-5">
          Welcome to Efo's Garage, your number one source for all cars new and old. We're dedicated to providing you the very best of cars, with an emphasis on quality, customer service, and uniqueness.
        </p>
        <div className="flex justify-center">
          <Link to="/products" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" replace>
            Browse Cars
          </Link>
        </div>
      </div>
      <h2 className="text-gray-500 text-center mt-4 mb-3">New Arrival</h2>
      <div className="container pb-5 px-lg-5">
        {/* <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 px-md-5">
        {products.map((product, index) => (
          <><FeatureProduct
            key={index}
            image={Image1} // You might need a default image or additional API to fetch images
            milelage={product.city_mpg}
            class_={product.class}
            combination_mpg={product.combination_mpg}
            cylinders={product.cylinders}
            displacement={product.displacement}
            drive={product.drive}
            fuel_type={product.fuel_type}
            make={product.make}
            model={product.model}
            transmission={product.transmission}
            year={product.year} />
            <FeatureProduct
              key={index}
              image={Image2} // You might need a default image or additional API to fetch images
              milelage={product.city_mpg}
              class_={product.class}
              combination_mpg={product.combination_mpg}
              cylinders={product.cylinders}
              displacement={product.displacement}
              drive={product.drive}
              fuel_type={product.fuel_type}
              make={product.make}
              model={product.model}
              transmission={product.transmission}
              year={product.year} /></> */}
        {/* ))} */}
        </div>
      {/* </div> */}
      <div className="flex flex-col bg-white py-4">
        <h5 className="text-center mb-3">Follow us on</h5>
        <div className="flex justify-center space-x-4">
          <a href="!#" className="text-blue-600 hover:text-blue-800">
            Facebook
          </a>
          <a href="!#" className="text-pink-600 hover:text-pink-800">
            Instagram
          </a>
          <a href="!#" className="text-blue-400 hover:text-blue-600">
            Twitter
          </a>
        </div>
      </div>
    </>
  );
}

export default Home;