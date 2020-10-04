Django Coding Challenge
=======================
Hi, this is the Django coding challenge. This challenge is designed to test your Django and Python skills.

Requirements
============
- Completed using Python v3.7
- Use Pipenv to manage packages - more on it: https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv
- Use SQLite
- Django version >= 2
- (Optional) Runs on docker and the application can be started with a single command `docker-compose up`
- The running application can be reached in the browser at *[host]:8080*
- The application is delivered with a sufficient admin reachable at *[host]:8080/admin*
- Delivered as a branch of this Bitbucket repository, pushed to the remote repository. Branch name should be YourFirstName_YourLastName e.g. Jan_Kowalski

Instructions on recreating base environment
========
1. Open terminal
2. Clone this repository
3. Navigate with cd commands into the project folder
4. Type in: `pipenv install`

If the above steps fail:
1. Make sure you have Pipenv installed. More on it: https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv
2. If installation is impossible feel free to use pip with requirements.txt AND Python 3.7

Scenario
========
You are asked to create a CRM for sales team in your company. The CRM is used by company's employees. The company is selling to customers three models of cars:
1. Red
2. Green 
3. Blue

!!!! You are asked to create a BACKEND application - i.e. no frontend-related code is necessary and will not be graded.

Task
====
This section describes which functionalities should the CRM submitted by you have:

1. (Django's admin panel) Ability to add users from - PLEASE SHARE WITH US USERNAME AND PASSWORD OF THE SUPERUSER
2. Users have the following characteristics:
    - first and last name
    - email - it has to have @anulujkredyt.pl in it
    - permission level - either basic or high
    - password
3. (Endpoint) User authentication - login is the email. Do not worry about security aspects. Tip: feel free to follow general guidelines for setting up basic authentication: https://docs.djangoproject.com/en/3.1/topics/auth/
4. (Endpoint) Ability to add customers with the following details:
    - first and last name
    - telephone - no more than 9 digits and no spaces
    - email - needs to have @ character in it
    - first and last name cannot repeat themselves. I.e. there can be Jan Nowak and Jerzy Nowak but there cannot be two people whose names and surnames are Jan Nowak.
    - only person with high permission level can add customer 
5. (Endpoint) Ability to list customers
    - possibility to filter customers who made purchase of a specific car - i.e. red car, green car etc.
6. (Endpoint) Ability to delete customers from the database - only person with high permission level can do that.
7. (Endpoint) Ability to edit customer details given customer's id
8. (Endpoint) Ability to add a purchase, many to one relationship with respect to custoemrs, with the following characteristics:
    - the following cars can be purchased: red, blue or green
9. (Endpoint) Ability to list all purchases inside a database with the following characteristics:
    - possibility to filter purchase of a specific car - i.e. red car, green car etc.
10. There has to be an API documentation, separate endpoint, which describes url addresses and their parameters/queries - tip: feel free to utilize Swagger or whatever other documentation tool
11. There has to be unit test coverage and you have to report on that coverage - tip: feel free to use external packages such as django-nose

!!!! You are asked to create a BACKEND application - i.e. no frontend-related code is necessary and will not be graded.

Restrictions
============
None! Use whatever tools / third party libraries you feel are necessary to complete the task. Feel free to consult whatever external resources you see fit. There is nothing wrong with using already existing resources. 