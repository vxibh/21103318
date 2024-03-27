'use client'
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function AllProductsPage() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      const response = await axios.get('http://20.244.56.144/test/companies/AMZ/categories/Laptop/products?top=10&minPrice=1&maxPrice=10000', {
        headers: {
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzExNTM0MzMyLCJpYXQiOjE3MTE1MzQwMzIsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjI2YWE1NzNjLWQ1YWItNGZiYS04MDI5LTY1ODY1YjcxOThjZCIsInN1YiI6IjIxMTAzMzE4QG1haWwuamlpdC5hYy5pbiJ9LCJjb21wYW55TmFtZSI6ImdvTWFydCIsImNsaWVudElEIjoiMjZhYTU3M2MtZDVhYi00ZmJhLTgwMjktNjU4NjViNzE5OGNkIiwiY2xpZW50U2VjcmV0IjoiTlBsWUl0Y3FBSWt5WlZuWSIsIm93bmVyTmFtZSI6IlZhaWJoYXYgU2hhcm1hIiwib3duZXJFbWFpbCI6IjIxMTAzMzE4QG1haWwuamlpdC5hYy5pbiIsInJvbGxObyI6IjIxMTAzMzE4In0.iZbcwNxUY1C2M0rMHZ5xaUehEcUOdluoiVRzyCtcKoo'
        }
      });
      console.log(response.data)
      setProducts(response.data);
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  };

  return (
    <div className="container">
      <h1 className="title">All Products</h1>
      <div className="product-list">
        {products.map(product => (
          <div key={product.productId} className="product-card">
            <h3>{product.productName}</h3>
            <p>Price: ${product.price}</p>
            <p>Rating: {product.rating}</p>
            <p>Discount: {product.discount}%</p>
            <p>Availability: {product.availability}</p>
            <Link to={`/product/${product.productId}`} className="btn">View Details</Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AllProductsPage;