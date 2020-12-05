import React, { useState } from 'react';
import ReactDOM from 'react-dom';

import { ProductPrice } from './components/ProductPrice';

document.addEventListener('DOMContentLoaded', (event) => {
  if (document.getElementById('product_price')) {
    let element = document.getElementById('product_price'),
      productId = element.dataset.productId;
    ReactDOM.render(
      <ProductPrice id={productId} />,
      document.getElementById('product_price')
    );
  }
});
