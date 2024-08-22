import { Link } from "react-router-dom";

function FeatureProduct({ image, milelage, class_, combination_mpg, cylinders, displacement, drive, fuel_type, make, model, transmission, year }) {
  return (
      <div className="col">
          <div className="bg-white rounded-lg shadow-sm">
              <img
                  className="w-full h-60 bg-black object-cover"
                  alt={`${make} ${model}`}
                  src={image}
              />
              <div className="p-4">
                  <h5 className="text-lg font-bold text-center">{make} {model}</h5>
                  <p className="text-center text-gray-500">Year: {year}</p>
                  <p className="text-center text-gray-500">Mileage: {milelage} MPG</p>
                  <p className="text-center text-gray-500">Class: {class_}</p>
                  <p className="text-center text-gray-500">MPG: {combination_mpg}</p>
                  <p className="text-center text-gray-500">Cylinders: {cylinders}</p>
                  <p className="text-center text-gray-500">Displacement: {displacement}L</p>
                  <p className="text-center text-gray-500">Drive: {drive}</p>
                  <p className="text-center text-gray-500">Fuel Type: {fuel_type}</p>
                  <p className="text-center text-gray-500">Transmission: {transmission}</p>
                  <div className="mt-4">
                      <Link
                          to={`/products/${make}-${model}-${year}`}
                          className="block w-full text-center border border-gray-800 text-gray-800 py-2 px-4 rounded hover:bg-gray-800 hover:text-white transition duration-300"
                      >
                          Detail
                      </Link>
                  </div>
              </div>
          </div>
      </div>
  );
}

export default FeatureProduct;
