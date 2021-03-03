# Cleaning Associate Requests Page :broom:

This application is efficinet way for managers acessing and stroing the requests from cleaning associates.
As new technologies arise, there must be changes done to an usual data management and processing :gem:

## The problem has to be solved 	:abacus:

The project idea was to create an responsive application serving a cleaning industry, where the 
employee/cleaner could login into the system and request the supplies from the manager needed 
to deliver the best cleaning experience. 
While working as a communal area cleaning associate I came across with 
an unreasonable need of contacting the manager on regular basis in order to inform him/her of the shortage of cleaning supplies. In most of the cases, the wrong supplies were ordered and delivered to the cleaner, rising a conflict between the manager and the employee. 

## Application Overview :bookmark_tabs: 

The current flask application is the prototype usefull for small cleaning companies, that would help to reduce time communicated with a manager about the supplies and increase the efficiency of cleaners work. Instead of personally contacting the manager, the cleaning associate could login into the system, see what requests he/she made in the past and add, update and delete the requests.

The main points were considered, while desinging the application:
 - Front end design using **FLask** framework, **python** coding language and **Jinja2** template engine
 - **CRUD** functionality ensuring ADD, UPDATE and DELETE functionalities
 - Working connection between the user input and **Flask-Mysql** database saving requests on **AWS RDS**
 - Set of tests **Unittest** checking the functionality of the application 

## Databases and User Inputs :fountain_pen:

The idea was to create a Relational Database connecting Table1 user credetials and Table2 supply requests. 
This was achieved in a MySQL Workbench, which was connected to the AWS database instance. Therefore, iputs were saved on the cloud. The diagram below visualises the relationship between two tables: 
<br>

![Screenshot (5)](https://user-images.githubusercontent.com/62849876/109809960-d89e9000-7c20-11eb-885f-8085102da03c.png)
<br>

When User logins, his/her credetials are saved in the database:
<br>
![page3pr](https://user-images.githubusercontent.com/62849876/109810190-21564900-7c21-11eb-90c1-ae050ac6a776.png)

<br>
After that the User is redirected to the home page, where all the past request's information is available to view, update
and delete. All requests are saved in the database, but in separate table and can be updated or deleted in a real time: 
<br>

![page7pr](https://user-images.githubusercontent.com/62849876/109810468-785c1e00-7c21-11eb-9b0e-c86735052757.png)

## User Interface :lotus_position:

The front page of the app looks the following:
<br>

![page2pr](https://user-images.githubusercontent.com/62849876/109810661-b9ecc900-7c21-11eb-8160-6593beafa047.png)

<br>
After this step the user is redirected to the Home page: 
<br>

![page4pr](https://user-images.githubusercontent.com/62849876/109810801-e6a0e080-7c21-11eb-8766-eac5bdcb44b7.png)
<br>
The user can type supplies needed in appropriate sections. When the user deletes the request, it dissappears from the 
table and from the database. However, if the user wants to update the request, he/she can press View button and see 
the following: 
<br>
![page8pr](https://user-images.githubusercontent.com/62849876/109811115-5616d000-7c22-11eb-9eee-236dd5121606.png)

After update request was submitted, reniewed version of the request is displays on home page and at tha database. 

## Testing
The testing has acieved 96% coverage meaning that the application is fully operational:
![coverage11111](https://user-images.githubusercontent.com/62849876/109811681-10a6d280-7c23-11eb-804d-a69337285970.png)




## Risk Assessment :mag:

During and After application deployment, the following must be considered: 
<br>
![riskassessmnt11111](https://user-images.githubusercontent.com/62849876/109811499-d2111800-7c22-11eb-9db5-5d047d13ecea.png)

