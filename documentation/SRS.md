<h2>Department App</h2>
## Vision

### "Department App" is a web application for managing departments and employees.

Application should provide:
- Registration and authorization.
- Storing departments and employees in database.
- Display list of departments and average salary of employees in these departments.
- Display list of all employees.
- Display list of employees for each department.
- Search for employees by birthday date.
- Searching employees born in specified period.
- Managing departments and employees (adding / editing / removing).
## 1. Homepage
On the home page user can see main information about this application. By clicking button 'Get started' unauthorized user will be redirected to log in and after login he will be redirected to departments page. 
Authorized user sees all buttons and can go to departments or employees page.
#### Main scenario:
- User opens a site;
- Application homepage is displayed.
![main page unauthorized](mockups/index_page.jpg)
Pic. 1.1 Homepage for unauthorized user.
![main page authorized](mockups/index_page_auth.jpg)
Pic. 1.2 Homepage for authorized user.
## 2. Login
### 2.1 Display the sign-in form
#### Main scenario:
User inputs data and signs in to account.
![login page](mockups/login.jpg)
Pic. 2.1 Login page.
## 3. Registration
### 3.1 Display the sign-up form.
#### Main scenario:
User inputs data and creates an account.
![registration page](mockups/register.jpg)
Pic. 3.1 Registration page.
## 4. Departments
### 4.1 Display list of departments
The mode is designed to view the list of departments.
#### Main scenario:
- User selects item "Departments";
- Application displays list of departments.
![departments page](mockups/departments_page.jpg)
Pic. 4.1 View the Department list.

The page displays the following items:
- Department title;
- Department description;
- Number of employees;
- Average salary.
### 4.2 Edit department
#### Main scenario:
- User clicks 'Edit' button in the departments list view mode;
- Application displays a popup window with input fields filled with current department data;
- User changes data and presses the "Save" button to save changes.
#### Cancel operation scenario:
- User clicks 'Edit' button in the departments list view mode;
- Application displays a popup window with input fields filled with current department data;
- User clicks '<b>x</b>' icon to close the window and cancel changes. 
![edit department](mockups/edit_dep.jpg)
Pic. 4.2 Editing a department.
### 4.3 Delete department
#### Main scenario:
- User clicks 'Delete' button in the departments list view mode;
- Application displays a popup window to confirm deleting;
- User clicks 'Yes' button to confirm deleting.
#### Cancel operation scenario:
- User clicks 'Delete' button in the departments list view mode;
- Application displays a popup window to confirm deleting;
- User clicks 'Cancel' button to cancel deleting.
![delete department](mockups/delete_dep.jpg)
Pic. 4.3 Deleting a department.
### 4.4 Add new department
#### Main scenario:
- User clicks 'Add new department' button on the departments page;
- Application redirects user to the page with form for adding a department;
- User inputs data and clicks 'Save' to save it to database.
#### Cancel operation scenario:
- User clicks 'Add new department' button on the departments page;
- Application redirects user to the page with form for adding a department.
- User clicks 'Cancel' to go back.
![add department page](mockups/add_dep.jpg)
Pic. 4.4 Adding new department.
## 5. Employees
### 5.1 Display list of employees
The mode is designed to view the list of employees.
#### Main scenario:
- User selects item "Employees";
- Application displays list of employees.
![employees page](mockups/employees_page.jpg)
Pic. 5.1 Employees page. 

The page displays the following items:
- Employee's full name;
- Employee's age;
- Employee's date of birth;
- Employee's salary;
- Employee's position;
- Employee's department;
### 5.2 Edit employee
#### Main scenario:
- User clicks 'Edit' button in the employees list view mode;
- Application displays a popup window with input fields filled with current employee data;
- User changes data and presses the "Save" button to save changes.
#### Cancel operation scenario:
- User clicks 'Edit' button in the employees list view mode;
- Application displays a popup window with input fields filled with current employee data;
- User clicks '<b>x</b>' icon to close the window and cancel changes. 
![edit employee](mockups/edit_emp.jpg)
Pic. 5.2 Editing an employee.
### 5.3 Delete employee
#### Main scenario:
- User clicks 'Delete' button in the employees list view mode;
- Application displays a popup window to confirm deleting;
- User clicks 'Yes' button to confirm deleting.
#### Cancel operation scenario:
- User clicks 'Delete' button in the employees list view mode;
- Application displays a popup window to confirm deleting;
- User clicks 'Cancel' button to cancel deleting.
![delete employee](mockups/delete_emp.jpg)
Pic. 5.3 Deleting an employee.
### 5.4 Add new employee
#### Main scenario:
- User clicks 'Add new employee' button on the employees page;
- Application redirects user to the page with form for adding an employee;
- User inputs data and clicks 'Save' to save it to database.
#### Cancel operation scenario:
- User clicks 'Add new employee' button on the employees page;
- Application redirects user to the page with form for adding an employee;
- User clicks 'Cancel' to go back.
![add employee page](mockups/add_emp.jpg)
Pic. 5.4 Adding new employee.