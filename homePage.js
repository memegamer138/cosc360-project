// Get elements
const navMenu = document.querySelector('nav ul');
const searchInput = document.querySelector('.search-bar input');
const searchButton = document.querySelector('#searchButton');
const featuredProducts = document.querySelector('.featured-products');
const categories = document.querySelector('.categories');

// Sample data for featured products
const products = [
  { id: 1, name: 'PS5', price: 49.99, image: 'images/product1.jpg' },
  { id: 2, name: 'Gaming Poster', price: 39.99, image: 'images/product2.jpg' },
  { id: 3, name: 'Keyboard', price: 29.99, image: 'images/product3.jpg' }
];

// Function to display featured products
function displayFeaturedProducts(products) {
  featuredProducts.innerHTML = ''; // Clear existing products
  products.forEach(product => {
    const productDiv = document.createElement('div');
    productDiv.classList.add('product');
    productDiv.innerHTML = `
      <h3>${product.name}</h3>
      <img src="${product.image}" alt="${product.name}">
      <p>$${product.price.toFixed(2)}</p>
      <button class="add-to-cart" data-id="${product.id}">Add to Cart</button>
    `;
    productDiv.querySelector('.add-to-cart').addEventListener('click', () => {
      window.location.href = 'cart.html';
    });
    featuredProducts.appendChild(productDiv);
  });
}

// Initial display of featured products
displayFeaturedProducts(products);

// Add event listeners
navMenu.addEventListener('click', (e) => {
  // Toggle navigation menu
  if (e.target.classList.contains('nav-link')) {
    navMenu.classList.toggle('open');
  }
});

searchButton.addEventListener('click', (e) => {
  // Handle search input
  e.preventDefault();
  alert('Search button clicked!');
  const searchTerm = searchInput.value.trim();
  if (searchTerm !== '') {
    // Search for games
    console.log(`Searching for "${searchTerm}"...`);
  }
});

categories.addEventListener('click', (e) => {
  // Filter games by category
  if (e.target.classList.contains('category-link')) {
    const category = e.target.textContent;
    console.log(`Filtering games by "${category}"...`);
  }
});