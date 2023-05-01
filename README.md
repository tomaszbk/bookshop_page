# Omega Bookshop's Web Simulation
Simulation of a bookshop's web page, where the focus is not in the design, but in the backend software managing url's routes, 
the connection with a database and user's accounts
Also includes the web scraper used

~~Check it out! https://omega-bookshop.herokuapp.com/~~ (NOTE: Currently migrating to aws due to heroku's new policies)

Made with: 

Python  
Django   
Sqlite  
Selenium  
Html, css, js 

### Main challenges overcomed:

* Implementing users with user carts,
* Product filtering,
* Liking products and avoiding a user to like more than 1 time a same product,
* Adding books with selenium scraping

## The scraper:
Using Selenium and Pandas, I scraped a local bookshop's web page to include some books in my catalog.  
Modified the resulting table by adding the 'likes' attribute, which will store the total amount of likes users have given the respective book
