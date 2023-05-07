# 📙Omega Bookshop's Web Simulation

### 📌 About the project
Simulation of a bookshop's web page, where the focus is in the backend management (Database connection, url's routes, user's accounts),  
and the book scraper to populate the tables.
The application is fully dockerized🐳 and portable to every environment  


<img src="https://github.com/kukelia/bookshop_page/blob/master/img/index.png" alt= “” width="950" height="550">

~~Check it out! https://omega-bookshop.herokuapp.com/~~ (NOTE: Currently migrating to aws due to heroku's new policies)

### 🖥️ Made with: 

- Python  
- Django   
- Sqlite  
- Selenium  
- Html, css, js 

### 🏆 Main challenges overcomed:

* Implementing users with user carts,
* Product filtering,
* Liking products and avoiding a user to like more than 1 time a same product,
* Adding books with selenium scraping

## 🤖 The scraper:
Using Selenium and Pandas, I scraped a local bookshop's web page to include some books in my catalog.  
The resulting table is transformed so it includes the 'likes' attribute, which will store the total amount of likes users have given the respective book

<img src="https://github.com/kukelia/bookshop_page/blob/master/img/products.png" alt= “” width="950" height="500">
