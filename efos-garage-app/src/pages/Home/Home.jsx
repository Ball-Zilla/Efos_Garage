// import Banner from "./Banner";
import FeatureProduct from "../../Components/FeatureProduct/FeatureProduct";
import ScrollToTopOnMount from "../../template/ScrollToTopOnMount";
import { Link } from "react-router-dom";
import Image1 from "../../Cars/B6VTQBN72BWQLQO6WXKGXQGM24-cr-540.jpg";
import Image2 from "../../Cars/2LIEITC5GFLANTHEYTRDWAHRJU-cr-540.jpg";
import Image3 from "../../Cars/ALLEIKYKFBTRNXLWWSS3FCQJG4-cr-540.jpg";

function Home() {
  return (
    <>
      <ScrollToTopOnMount />
      {/* <Banner /> */}
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
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 px-md-5">
          <FeatureProduct
            image={Image1}
            title="Mercedes C50"
            description="4matic"
            productId="1"
          />
          <FeatureProduct
            image={Image2}
            title="BMW X5"
            description="xDrive"
            productId="2"
          />
          <FeatureProduct
            image={Image3}
            title="Audi Q7"
            description="Quattro"
            productId="3"
          />
        </div>
      </div>
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