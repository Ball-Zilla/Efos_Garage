import React from "react";
import { Link } from "react-router-dom";

function FeatureProduct({ image, title, description, productId }) {
    return (
        <div className="col">
            <div className="bg-white rounded-lg shadow-sm">
                <img
                    className="w-50 h-60 bg-black object-cover"
                    alt=""
                    src={image}
                />
                <div className="p-4">
                    <h5 className="text-lg font-bold text-center">{title}</h5>
                    <p className="text-center text-gray-500">{description}</p>
                    <div className="mt-4">
                        <Link
                            to={`/products/${productId}`}
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