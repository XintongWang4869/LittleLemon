# Little Lemon Restaurant Web Application

The Little Lemon Restaurant project connects the restaurant back-end to a MySQL database. This project includes the setup of a booking system and menu display using Django REST Framework (DRF).

Features:
* Database Integration: Successfully connected the Little Lemon restaurant back-end to a MySQL database.

* Booking API: Implemented a RESTful Table Booking API to facilitate reservations. This API allows customers to book a table for dining on a specific date and for a certain number of people.

* Menu API: Developed a Menu API to display food items available for ordering. Customers can view the menu and select items to order.



**See [here](./instructions.md) for a detailed step-by-step guide to replicate this project.**


<br>

## Demo

**Index page:** restaurant/

<img src="demo/restaurant-idx-page.png" alt="Little Lemon" width="500px">

**Menu items:** restaurant/menu/

<img src="demo/restaurant-menu-endpoint.png" alt="Little Lemon" width="500px">

**Booking endpoint:** restaurant/booking/

<img src="demo/restaurant-booking-endpoint.png" alt="Little Lemon" width="500px">

**Booking information:** restaurant/booking/tables

<img src="demo/restaurant-booking-tables-endpoint.png" alt="Little Lemon" width="500px">


**Testing:**

* Unit test     
<img src="demo/unittest-passed.png" alt="Little Lemon" width="500px">

* Insomnia   
    * POST - add a new menu item    
    <img src="demo/insomnia-test-menu-post.png" alt="Little Lemon" width="500px">
    * GET - get menu items    
    <img src="demo/insomnia-test-menu-get.png" alt="Little Lemon" width="500px">
    * PUT - update an existing menu item    
    <img src="demo/insomnia-test-menu-put.png" alt="Little Lemon" width="500px">
    * Accessing a protected page without token    
    <img src="demo/insomnia-without-token.png" alt="Little Lemon" width="500px">
    * Accessing a protected page with token    
    <img src="demo/insomnia-with-token.png" alt="Little Lemon" width="500px">


## Note

This project is currently in the development stage. Two things need to be noted:
- **Environment Setup:** The repository does not contain a pre-configured environment. Users will need to create and configure their own virtual environment to manage dependencies.
- **MySQL Database:** The project uses a MySQL database configured with data that resides only on the developer's local machine. Users will need to set up their own local MySQL database and configure the connection settings in the project.

